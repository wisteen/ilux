from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

from django.utils import timezone
from .constants import *
from django.utils.text import slugify


from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
import random
import string


from django.db import transaction


def generate_unique_slug(instance, name):
    slug = slugify(name)
    model_class = instance.__class__
    unique_slug = slug
    counter = 1

    while model_class.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='author_profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_subscribed_to_newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    ICON_CHOICES = [
        ('fa-laptop', 'Laptop'),
        ('fa-mobile-alt', 'Mobile'),
        ('fa-tshirt', 'T-shirt'),
        ('fa-home', 'Home'),
        ('fa-car', 'Car'),
        ('fa-book', 'Book'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-laptop')
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_image/")
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    description = RichTextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    colors = models.ManyToManyField('Color', blank=True)
    sizes = models.ManyToManyField('Size', blank=True)
    details = RichTextField(blank=True, null=True)
    shipping_info = models.TextField(blank=True, null=True)
    size_guidance = RichTextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    product_code = models.CharField(max_length=8, unique=True, editable=False, blank=True, null=True)
    stock = models.IntegerField(default=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discount(self):
        if self.old_price and self.new_price:
            return round((self.old_price - self.new_price) / self.old_price * 100, 2)
        return None

    @property
    def is_available(self):
        return self.stock > 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)

        if not self.product_code:
            self.product_code = self.generate_product_code()


        super().save(*args, **kwargs)

    def generate_product_code(self):
        prefix = 'IHM'
        suffix = ''.join(random.choices(string.digits, k=5))
        return f"{prefix}{suffix}"

    def average_rating(self):
        ratings = Rating.objects.filter(product=self)
        if ratings.count() == 0:
            return 0
        cal = sum(rating.rating for rating in ratings) / ratings.count()
        return round(cal, 1)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, help_text="Hex color code (e.g., #FFFFFF)")

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="wishlist", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="wishlists")

    def __str__(self):
        return f"Wishlist of {self.user.username}"

    def add_product(self, product):
        """Add a product to the wishlist if not already present."""
        if not self.products.filter(id=product.id).exists():
            self.products.add(product)

    def remove_product(self, product):
        """Remove a product from the wishlist."""
        self.products.remove(product)

    def clear_wishlist(self):
        """Remove all products from the wishlist."""
        self.products.clear()



class Compare(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="compare", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="compares")

    def __str__(self):
        return f"Comparison list of {self.user.username}"


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    products = models.ManyToManyField(Product, related_name="promotions")

    def is_active(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating out of 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="cart", on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='CartItem')

    def total_cost(self):
        return sum(item.product.new_price * item.quantity for item in self.cartitem_set.all())

    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    def checkout(self, address, delivery_instruction=None):
        # Validate address
        if not address or address.user != self.user:
            raise ValueError("Invalid address provided for checkout.")
        
        # Start a database transaction to ensure atomicity
        with transaction.atomic():
            # Create a new order
            order = Order.objects.create(
                user=self.user,
                address=address,
                delivery_instruction=delivery_instruction,
                total_cost=0,  # Will calculate and update later
                status='PENDING'
            )

            total_cost = 0

            # Transfer CartItem data to OrderItem
            for item in self.cartitem_set.all():
                if item.quantity > item.product.stock:
                    raise Exception(f"Insufficient stock for {item.product.name}")

                # Deduct stock
                item.product.stock -= item.quantity
                item.product.save()

                # Create OrderItem
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.new_price,  # Use product's current price
                )

                # Add to total cost
                total_cost += (item.product.new_price * item.quantity) + address.state.delivery_charge

            # Update total cost in the order
            order.total_cost = total_cost
            order.save()

            # Clear the cart
            self.cartitem_set.all().delete()

        return order


    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def clean(self):
        if self.quantity > self.product.stock:
            raise ValidationError(f"Not enough stock for {self.product.name}.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensures clean() is called
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Cart: {self.cart.user.username})"


class Rating(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='ratings')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="rate", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    headline = models.CharField(max_length=255, blank=True, null=True)
    media = models.FileField(upload_to="rating_media/", null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.rating} - {self.product.name} by {self.user.username}'

    def get_author_profile_picture(self):
        # Access the Author profile picture through the User
        return self.user.profile.profile_picture.url if self.user.profile.profile_picture else None


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="addresses", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., Home, Office
    street = models.TextField()
    city = models.CharField(max_length=100)
    state = models.ForeignKey('DeliveryZone', related_name='addresses', on_delete=models.SET_NULL, null=True)  # Changed to ForeignKey
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

    def save(self, *args, **kwargs):
        if self.is_default:
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)


class DeliveryZone(models.Model):
    zone_name = models.CharField(max_length=100)  # e.g., Local, Regional, International
    estimated_time = models.CharField(max_length=100)  # e.g., "1-3 Days"
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.zone_name



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name="orders", on_delete=models.SET_NULL, null=True)
    delivery_instruction = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('COMPLETED', 'Completed'),
            ('CANCELLED', 'Cancelled')
        ],
        default='PENDING'
    )

    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at the time of order

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"



class Payment(models.Model):
    order = models.OneToOneField(Order, related_name="payment", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("Success", "Success"), ("Failed", "Failed"), ("Pending", "Pending")],
        default="Pending",
    )

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.status}"




class Schedule(models.Model):
    date = models.DateField()
    day_of_week = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.day_of_week} - {self.date}"

class TimeSlot(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="timeslots")
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Free', 'Free')])

    def __str__(self):
        return f"{self.start_time} - {self.end_time} ({self.status})"






class ContactInquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Leadership(models.Model):
    about_us = models.ForeignKey(AboutUs, related_name='leaders', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leadership/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

class KeyFigure(models.Model):
    about_us = models.ForeignKey(AboutUs, related_name='key_figures', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.label}: {self.value}"


class PageContent(models.Model):
    PAGE_TYPE_CHOICES = [
        ('Become a Drop Shipper', 'Become a Drop Shipper'),
        ('Promo & Deals', 'Promo & Deals'),
        ('Get to know Us', 'Get to know Us'),
        ('For Consumers', 'For Consumers'),
    ]
    page_type = models.CharField(max_length=255, choices=PAGE_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_page_type_display()} - {self.title}"