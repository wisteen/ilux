from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, CartItem, Cart
from django.utils import timezone
from django.db.models import Count, Avg, Q
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# Create your views here.
import json
from django.shortcuts import render, get_object_or_404
from .models import Profile, AboutUs, ContactInquiry, Category, Product, ProductImage, Wishlist, Compare, Promotion, Review, Cart, Address, DeliveryZone, Schedule, TimeSlot, Order

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from webdata.models import HeroSlide, Banner, WebPage

from django import forms
# Homepage view: Display products and categories
def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.select_related('category').prefetch_related('images')[:10]  # limit to 10 products for example
    promotions = Promotion.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    banners = Banner.objects.filter(is_active=True).order_by('order')
    web_page = WebPage.objects.filter(is_published=True).first()
    # Assume trending based on most viewed categories (customize as needed)
    trending_categories = Category.objects.annotate(
        product_count=Count('products')
    ).order_by('-product_count')[:6]  # Top 5 trending categories by product count

    half = len(categories) // 2
    left_categories = categories[:half]
    right_categories = categories[half:]

    # Fetch the top 5 most popular products based on views
    popular_products = Product.objects.order_by('-views')[:5]  # Top 5 products by views


    # Fetch latest products with related images (prefetching for efficiency)
    latest_products = Product.objects.prefetch_related('images').order_by('-created_at')[:10]  # Adjust number as needed
    

    all_products = Product.objects.all()
    wishlist = []

    if request.user.is_authenticated:
        wishlist_obj, _ = Wishlist.objects.get_or_create(user=request.user)
        wishlist = wishlist_obj.products.values_list('id', flat=True)

    context = {
        'categories': categories,
        'products': products,
        'promotions': promotions,
        'trending_categories': trending_categories,
        'popular_products': popular_products,
        'latest_products': latest_products,
        "wishlist": wishlist,
        "slides": slides,
        "banners": banners,
        "web_page": web_page,
        'left_categories': left_categories,
        'right_categories': right_categories,
    }
    return render(request, 'index.html', context)
def category_detail_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})

    
# Product detail view: Show details of a selected product
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    reviews = product.reviews.select_related('user')  # Reviews related to the product
    product.views = models.F('views') + 1  # Increment the view count
    product.save(update_fields=['views'])
    
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)

# Category view: Show products in a specific category
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_detail.html', context)

@login_required
def wishlist_count(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    total_products = wishlist.products.count()
    return JsonResponse({"total_products": total_products})

    

# @login_required
def get_cart_data(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = [
        {
            "id": item.id,
            "product_name": item.product.name,
            "quantity": item.quantity,
            "price": item.product.new_price,
            "image_url": item.product.image.url,
        }
        for item in cart.cartitem_set.all()
    ]
    data = {
        "total_cost": cart.total_cost(),
        "total_items": cart.total_items(),
        "cart_items": cart_items,
    }
    return JsonResponse(data)





def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Get or create a CartItem for this product
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Increase the quantity if item is already in cart
        if not created:
            cart_item.quantity += 1
        cart_item.save()

        # Optionally return cart info as JSON
        return JsonResponse({
            "total_items": cart.total_items(),
            "total_cost": float(cart.total_cost()),
            "product_image":cart_item.product.image.url,
            "message": "Item added to cart!"
        })
    else:
        return JsonResponse({"error": "User not authenticated"}, status=403)




def get_product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(product=product)
    data = {
        "id": product.id,
        "name": product.name,
        "category": product.category.name if product.category else "",
        "new_price": product.new_price,
        "old_price": product.old_price,
        "discount": product.discount,
        "product_main_img":product.image.url,
        "image_urls": [img.image.url for img in product_images],  # Add more URLs if multiple images exist
        "description": product.description,
        "availability": "In Stock" if product.stock > 0 else "Out of Stock",
        "shipping_info": product.shipping_info,
    }
    return JsonResponse(data)




@require_http_methods(["DELETE"])
def remove_cart_item(request, item_id):
    try:
        # Get the CartItem by ID and delete it
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()

        # Respond with success
        return JsonResponse({"success": True, "message": "Item removed from cart."})
    except Exception as e:
        # Respond with error message if something goes wrong
        return JsonResponse({"success": False, "message": str(e)}, status=400)

@csrf_exempt
def update_cart_item_quantity(request, item_id):
    """
    Update the quantity of a cart item.
    """
    if request.method == "POST":
        try:
            # Fetch the cart item by ID
            cart_item = get_object_or_404(CartItem, id=item_id)
            
            # Parse the new quantity from the request body
            import json
            data = json.loads(request.body)
            new_quantity = data.get("quantity", None)

            if new_quantity is None or new_quantity < 1:
                return JsonResponse({
                    "success": False, 
                    "message": "Quantity must be at least 1."
                }, status=400)
            
            # Check if stock is sufficient
            if new_quantity > cart_item.product.stock:
                return JsonResponse({
                    "success": False, 
                    "message": "Insufficient stock available."
                }, status=400)
            
            # Update quantity and save
            cart_item.quantity = new_quantity
            cart_item.save()

            # Return updated cart summary
            cart = cart_item.cart
            return JsonResponse({
                "success": True,
                "total_items": cart.total_items(),
                "total_cost": cart.total_cost()
            })

        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({
            "success": False,
            "message": "Invalid request method."
        }, status=405)



def get_header_cart_data(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = [{
            "id": item.id,
            "product_name": item.product.name,
            "product_url": item.product.get_absolute_url(),
            "product_image": item.product.image.url,
            "quantity": item.quantity,
            "price": float(item.product.new_price),
        } for item in cart.cartitem_set.all()]

        return JsonResponse({
            "total_items": cart.total_items(),
            "total_cost": float(cart.total_cost()),
            "items": cart_items,
        })
    return JsonResponse({"error": "User not authenticated"}, status=403)



@login_required
def toggle_wishlist(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        if product in wishlist.products.all():
            wishlist.products.remove(product)
            action = "removed"
        else:
            wishlist.products.add(product)
            action = "added"

        return JsonResponse({"success": True, "action": action, "product_id": product_id})
    
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)




def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:10]
    cart = Cart.objects.get(user=request.user)
    cart_item = cart.cartitem_set.filter(product=product).first()

    ratings = product.ratings.all()
    total_arr = [rating.rating for rating in ratings]
    total_ratings = len(total_arr)

    count_1 = total_arr.count(1)
    count_2 = total_arr.count(2)
    count_3 = total_arr.count(3)
    count_4 = total_arr.count(4)
    count_5 = total_arr.count(5)

    # Calculating percentages
    percent_1 = (count_1 / total_ratings) * 100 if total_ratings else 0
    percent_2 = (count_2 / total_ratings) * 100 if total_ratings else 0
    percent_3 = (count_3 / total_ratings) * 100 if total_ratings else 0
    percent_4 = (count_4 / total_ratings) * 100 if total_ratings else 0
    percent_5 = (count_5 / total_ratings) * 100 if total_ratings else 0

    # Precomputed values
    rating_details = [
        {"rating": 5, "percent": percent_5},
        {"rating": 4, "percent": percent_4},
        {"rating": 3, "percent": percent_3},
        {"rating": 2, "percent": percent_2},
        {"rating": 1, "percent": percent_1},
    ]
    
    context = {
        'product': product,
        'related_products': related_products,
        'cart_item': cart_item,  # Pass CartItem to the template
        'ratings': ratings,
        'rating_details': rating_details,
    }
    return render(request, 'pages/shop-single.html', context)


from django import forms
from .models import Rating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['headline', 'review', 'rating', 'media']
        widgets = {
            'review': forms.Textarea(attrs={'placeholder': 'What did you like or dislike? What did you use this product for?', 'rows': 3}),
        }
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating not in range(1, 6):
            raise forms.ValidationError("Please select a valid rating between 1 and 5.")
        return rating

def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user has already reviewed the product
    if Rating.objects.filter(product=product, user=request.user).exists():
        messages.error(request, "You have already reviewed this product.")
        return redirect('product_detail', slug=product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()
            messages.success(request, "Your review has been submitted successfully.")
            return redirect('product_detail', slug=product.slug)
        else:
            return render(request, 'pages/shop-single.html', {'form': form, 'product': product})
    else:
        form = ReviewForm()
    return render(request, 'pages/shop-single.html', {'form': form, 'product': product})

def wishlist(request):
    return render(request, 'pages/shop-wishlist.html', {})

@login_required
def get_wishlist(request):
    user = request.user
    wishlist = user.wishlist  # Access the Wishlist via the `related_name`
    products = wishlist.products.all()
    product_list = [{
        "id": product.id,
        "name": product.name,
        "price": product.new_price,
        "image": product.image.url,  # Assuming `Product` has an `image` field
        "in_stock": product.stock,  # Assuming `Product` has an `in_stock` field
    } for product in products]

    return JsonResponse({"products": product_list})





@csrf_exempt
@require_POST
def remove_from_wishlist(request):
    try:
        data = json.loads(request.body)
        product_id = data.get("product_id")
        wishlist = Wishlist.objects.get(user=request.user)  # Fetch the user's wishlist
        product = Product.objects.get(id=product_id)  # Get the product instance
        wishlist.remove_product(product)  # Remove the product using the method
        return JsonResponse({"message": "Product removed from wishlist."})
    except Wishlist.DoesNotExist:
        return JsonResponse({"message": "Wishlist not found."}, status=404)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Product not found."}, status=404)
    except Exception as e:
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=400)






@login_required
def checkout_view(request):
    """
    Checkout view using Cart and CartItem instead of Order and OrderItems.
    """
    user = request.user
    addresses = Address.objects.filter(user=user)
    delivery_zones = DeliveryZone.objects.all()
    schedules = Schedule.objects.all()
    time_slots = TimeSlot.objects.all()

    # Fetch the user's cart
    cart = get_object_or_404(Cart, user=user)
    cart_items = cart.cartitem_set.all()

    # Calculate totals
    cart_total = cart.total_cost()
    form = AddressForm()

    if request.method == 'POST':
        # Handle form submission
        address_id = request.POST.get('selected_address')
        delivery_instruction = request.POST.get('delivery_instruction')

        # Validate address
        try:
            address = Address.objects.get(id=address_id, user=request.user)
        except Address.DoesNotExist:
            messages.error(request, "Invalid address selection.")
            return redirect('checkout')

        # Perform checkout
        try:
            order = cart.checkout(address=address, delivery_instruction=delivery_instruction)
            messages.success(request, "Order placed successfully!")
            return redirect('order_success', order_id=order.id)
        except Exception as e:
            messages.error(request, str(e))
            print(e)
            return redirect('checkout')

    
    context = {
        "addresses": addresses,
        "delivery_zones": delivery_zones,
        "cart_items": cart_items,
        "cart_total": cart_total,
        'schedules': schedules,
        'time_slots': time_slots,
        "form": form, 
    }
    return render(request, "pages/shop-checkout.html", context)


@login_required
def place_order(request):
    """
    Handle placing an order.
    """
    if request.method == "POST":
        address_id = request.POST.get("selected_address")
        delivery_zone_id = request.POST.get("delivery_zone")
        payment_method = request.POST.get("payment_method")
        delivery_instruction = request.POST.get("delivery_instruction", "")

        # Validate Address and Delivery Zone
        address = get_object_or_404(Address, id=address_id, user=request.user)
        delivery_zone = get_object_or_404(DeliveryZone, id=delivery_zone_id)

        # Get the cart and its items
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return JsonResponse({"error": "Your cart is empty!"}, status=400)

        # Calculate total cost
        cart_total = sum(item.product.price * item.quantity for item in cart_items)
        total_cost = cart_total + delivery_zone.delivery_charge

        # Create the Order
        order = Order.objects.create(
            user=request.user,
            address=address,
            delivery_zone=delivery_zone,
            delivery_instruction=delivery_instruction,
            payment_method=payment_method,
            total_cost=total_cost,
            is_paid=False,  # Assume payment happens later
        )

        # Add items to the order
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # Clear the cart
        cart_items.delete()

        return JsonResponse({
            "message": "Order placed successfully!",
            "order_id": order.id,
            "total_cost": total_cost,
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def calculate_delivery_charge(request):
    """
    Calculate delivery charges based on the selected delivery zone.
    """
    if request.method == "GET":
        delivery_zone_id = request.GET.get("delivery_zone")
        delivery_zone = get_object_or_404(DeliveryZone, id=delivery_zone_id)
        return JsonResponse({
            "delivery_charge": delivery_zone.delivery_charge,
            "estimated_time": delivery_zone.estimated_time,
        })

    return JsonResponse({"error": "Invalid request"}, status=400)




from django import forms

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'name', 'street', 'city', 'state', 'country',
            'postal_code', 'phone_number', 'is_default',
        ]

        widgets = {
            'name': forms.Select(choices=[
                ('Home', 'Home'),
                ('Work', 'Work'),
                ('Office', 'Office'),
                ('Other', 'Other')
            ], attrs={'class': 'form-select'}),

            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return JsonResponse({"message": "Address added successfully!"})
        else:
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)



@login_required
def address_list(request):
    """
    Display a list of the user's addresses.
    """
    addresses = Address.objects.filter(user=request.user)
    return render(request, "address/address_list.html", {"addresses": addresses})


@login_required
def edit_address(request, pk):
    """
    Handle editing an existing address.
    """
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Address updated successfully!"})
        return JsonResponse({"error": form.errors}, status=400)
    else:
        form = AddressForm(instance=address)
    return render(request, "address/edit_address.html", {"form": form, "address": address})


def delete_address(request, address_id):
    if request.method == 'POST':
        address = get_object_or_404(Address, id=address_id)

        # Check if the address is default
        if address.is_default:
            return JsonResponse({'success': False, 'message': 'You cannot delete the default address.'}, status=400)

        # Delete the address
        address.delete()

        return JsonResponse({'success': True, 'message': 'Address deleted successfully.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)


@login_required
def set_default_address(request, pk):
    """
    Set an address as the default.
    """
    address = get_object_or_404(Address, pk=pk, user=request.user)
    # Set all other addresses as non-default
    Address.objects.filter(user=request.user, is_default=True).update(is_default=False)
    # Set the selected address as default
    address.is_default = True
    address.save()
    return JsonResponse({"message": "Default address updated successfully!"})


@login_required
def order_success_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'pages/order_success.html', {'order': order})


from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import Order
import requests

def make_payment(request, order_id):
    # Fetch the order
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Flutterwave Payment API Endpoint
    flutterwave_url = "https://api.flutterwave.com/v3/payments"

    # Prepare Payment Data
    payment_data = {
        "tx_ref": f"tx-{order.id}-{request.user.id}",
        "amount": float(order.total_cost),
        "currency": "NGN",  # Change to your currency, e.g., "NGN"
        "redirect_url": request.build_absolute_uri(f"/payment/callback/{order.id}/"),
        "customer": {
            "email": request.user.email,
            "phonenumber": request.user.profile.phone_number,
            "name": request.user.get_full_name(),
        },
        "customizations": {
            "title": "Order Payment",
            "description": f"Payment for Order #{order.id}",
        },
    }

    # Make API Request to Flutterwave
    headers = {
        "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(flutterwave_url, json=payment_data, headers=headers)
    response_data = response.json()

    # Check Response
    if response.status_code == 200 and response_data.get("status") == "success":
        payment_link = response_data["data"]["link"]
        return redirect(payment_link)
    else:
        return JsonResponse({"error": "Payment initiation failed", "details": response_data}, status=400)

def payment_callback(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Check payment status
    status = request.GET.get("status", "")
    tx_ref = request.GET.get("tx_ref", "")
    transaction_id = request.GET.get("transaction_id", "")

    if status == "successful":
        # Verify the payment with Flutterwave
        verification_url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"
        headers = {
            "Authorization": f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
        }
        response = requests.get(verification_url, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status") == "success":
            # Update order as paid
            order.is_paid = True
            order.status = "COMPLETED"
            order.save()
            return render(request, "payment_success.html", {"order": order})

    # Handle failed or cancelled payments
    order.status = "CANCELLED"
    order.save()
    return render(request, "payment_failed.html", {"order": order})




class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 4,
            }),
        }

def contact_us(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! Your inquiry has been submitted.")
            return redirect('contact_us')
    else:
        form = ContactInquiryForm()

    return render(request, 'pages/contact.html', {'form': form})


def about_us(request):
    # Fetch the latest AboutUs content
    about_us_content = AboutUs.objects.last()
    return render(request, 'pages/about.html', {'about_us': about_us_content})


from django.db.models import Q
from django.http import JsonResponse

def products_view(request):
    """
    Handle product search and category filtering with additional filters.
    """
    category_slug = request.GET.get('category')  # Fetch the category slug
    search_query = request.GET.get('q')         # Fetch the search query
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_rating = request.GET.get('min_rating')

    filters = Q()

    # Filter by category
    if category_slug:
        filters &= Q(category__slug=category_slug)

    # Filter by search query
    if search_query:
        filters &= Q(name__icontains=search_query) | Q(description__icontains=search_query)

    # Price range filtering
    if min_price:
        try:
            min_price = float(min_price)
            filters &= Q(new_price__gte=min_price)
        except ValueError:
            pass  # Handle invalid price input

    if max_price:
        try:
            max_price = float(max_price)
            filters &= Q(new_price__lte=max_price)
        except ValueError:
            pass  # Handle invalid price input

    # Average rating filter
    products = Product.objects.all()
    if min_rating:
        try:
            min_rating = float(min_rating)
            products = products.annotate(average_rating=Avg('reviews__rating'))
            filters &= Q(average_rating__gte=min_rating)
        except ValueError:
            pass  # Handle invalid rating input

    # Apply all filters
    products = products.filter(filters).select_related('category').prefetch_related('reviews')

    # Serialize the results
    product_data = [
        {
            "name": product.name,
            "slug": product.slug,
            "image": product.image.url if product.image else None,
            "price": product.new_price,
            "old_price": product.old_price,
            "rating": product.average_rating or 0,  # Avoid None if no ratings
            "is_available": product.is_available,
            "category": product.category.name,
        }
        for product in products
    ]

    return JsonResponse({"products": product_data})


def filter_page(request):
    # Get the search term (if any) from the GET parameters
    search_query = request.GET.get('search', '')

    # Get all products (or stores, if using a Store model), or filter by search query if provided
    stores = Product.objects.all()  # Change to Store if you're filtering stores
    products_data = None

    if search_query:
        stores = stores.filter(name__icontains=search_query)

        if stores:
            # Convert from queryset to list
            products_data = []
            for product in stores:
                average_rating = product.average_rating()

                filtered_product = {
                    "id": product.id,
                    "name": product.name,
                    "price": product.discount,
                    "average_rating": average_rating,
                    "image": f'http://127.0.0.1:8000{product.image.url}' if product.image else None,
                }

                products_data.append(filtered_product)
        else:
            products_data = []

    return render(request, 'pages/shop-grid.html', {'stores': products_data, 'search_query': search_query})


def filter_api(request):
    if request.method == "GET":
        # Extract query parameters
        search_query = request.GET.get('search', '')
        ratings = request.GET.getlist('ratings', '')
        categories = request.GET.getlist('categories', '')
        min_price = request.GET.get('min_price', None)
        max_price = request.GET.get('max_price', None)
        page = request.GET.get('page')
        page_size = request.GET.get('size')

        # Validating page and page_size values
        if page is not None:
            try:
                page = int(page)
            except ValueError:
                page = 1

        if page_size is not None:
            try:
                page_size = int(page_size)
            except ValueError:
                page_size = 3

        # Set default page value if none was provided.
        if page is None:
            page = 1

        # Set default page_size value if none was provided.
        if page_size is None:
            page_size = 3


        ratings_list = []
        categories_list = []

        # Get ratings list
        if ratings != [''] and ratings is not None and ratings != '':
            for values in ratings:
                ratings_list = values.split(',')

        # Get categories list
        if categories != [''] and categories is not None and categories != '':
            for values in categories:
                categories_list = values.split(',')

        # Query to get all products
        products = Product.objects.all().order_by('-created_at')

        # Filter by ratings
        if len(ratings_list) > 0:
            query = Q()

            for rating in ratings_list:
                try:
                    int(rating)
                except ValueError:
                    rating = 5
                except TypeError:
                    rating = 5

                query |= Q(avg_rating__gte=rating, avg_rating__lt=int(rating) + 1)

            products = (
                products.annotate(avg_rating=Avg('ratings__rating')).filter(query)
            )

        # Filter by categories
        if len(categories_list) > 0:
            # Get the id of each category in the list and add them to a new list.
            categories_obj_list = [Category.objects.get(name=category) for category in categories_list]
            products = products.filter(category__in=categories_obj_list)

        # Filter by minimum and maximum price
        if min_price is not None and max_price is not None:
            products = products.filter(new_price__range=(min_price, max_price))
        elif min_price is None and max_price is not None:
            products = products.filter(new_price__lte=max_price)
        elif min_price is not None and max_price is None:
            products = products.filter(price__gte=min_price)

        if search_query:
            products = products.filter(category__name__icontains=search_query)

        # Pagination
        paginator = Paginator(products, per_page=page_size, orphans=0)
        try:
            paginated_data = paginator.page(page)
            total_pages = paginator.num_pages
        except EmptyPage:
            return JsonResponse({"error": 'Page not found.'}, status=404)
        except PageNotAnInteger:
            return JsonResponse({"error": 'Page number must be an integer.'}, status=400)

        # Convert from queryset to serializable data
        products_data = []

        for product in paginated_data:
            average_rating = product.average_rating()
            reviews_count = product.reviews.all().count()

            filtered_product = {
                "id": product.id,
                "name": product.name,
                "discount": round(product.discount, 2),
                "price": round(product.new_price, 2),
                "old_price": round(product.old_price, 2),
                "average_rating": average_rating,
                "category": product.category.name,
                "reviews_count": reviews_count,
                "image": f'http://127.0.0.1:8000{product.image.url}' if product.image else None,
            }

            products_data.append(filtered_product)

        # Get next and previous pages url.
        if page == 1 and page == total_pages:
            previous_page = None
            next_page = None
        elif page == 1 and page < total_pages:
            previous_page = None
            next_page = f"https://{get_current_site(request).domain}"\
                        f"{reverse('filter_api')}?page={page + 1}&size={page_size}"
        if page > 1 and page < total_pages:
            previous_page = f"https://{get_current_site(request).domain}"\
                            f"{reverse('filter_api')}?page={page - 1}"\
                            f"&size={page_size}"
            next_page = f"https://{get_current_site(request).domain}"\
                        f"{reverse('filter_api')}?page={page + 1}&size={page_size}"
        if page > 1 and page == total_pages:
            previous_page = f"https://{get_current_site(request).domain}"\
                            f"{reverse('filter_api')}?page={page - 1}"\
                            f"&size={page_size}"
            next_page = None

        # Response data
        data = {
            'total_number_of_products': len(products),
            'total_pages': total_pages,
            'previous_page': previous_page,
            'current_page': page,
            'next_page': next_page,
            'products': products_data
        }

        # Return the filtered results
        return JsonResponse({"products": data}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)




def error_400_view(request, exception):
    return render(request, 'home/400.html', status=400)

def error_403_view(request, exception):
    return render(request, 'home/403.html', status=403)

def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

def error_500_view(request):
    return render(request, 'home/500.html', status=500)

def error_401_view(request, exception=None):
    return render(request, 'home/401.html', status=401)