from django.contrib import admin
from .models import (
    Profile, Category, Product, ProductImage, Color, Size, Wishlist, Compare, Schedule, TimeSlot,
    Promotion, Cart, CartItem, Rating, ContactInquiry, AboutUs, Leadership, KeyFigure
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'state', 'country')
    search_fields = ('user__username', 'phone_number', 'city', 'state', 'country')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('icon',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'new_price', 'old_price', 'discount', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')
    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(Compare)
class CompareAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percentage', 'start_date', 'end_date', 'is_active')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)

    def is_active(self, obj):
        return obj.is_active()
    is_active.boolean = True  # Shows as a checkmark in the admin
    is_active.short_description = 'Active'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username')


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_cost')
    search_fields = ('user__username',)
    inlines = [CartItemInline]

    def total_cost(self, obj):
        return obj.total_cost()
    total_cost.short_description = 'Total Cost'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__username', 'product__name')




from django.contrib import admin
from .models import Address, DeliveryZone, Order, OrderItem, Payment

# Register Address Model
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "city", "state", "country", "is_default")
    list_filter = ("is_default", "country")
    search_fields = ("user__username", "name", "city", "state", "country")

# Register DeliveryZone Model
@admin.register(DeliveryZone)
class DeliveryZoneAdmin(admin.ModelAdmin):
    list_display = ("zone_name", "estimated_time", "delivery_charge")
    search_fields = ("zone_name",)

# Inline Order Items for Order Admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of blank fields for adding new items

# Register Order Model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_cost", "is_paid", "created_at")
    list_filter = ("is_paid", "created_at")
    search_fields = ("user__username", "id")
    inlines = [OrderItemInline]

# Register Payment Model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "payment_method", "transaction_id", "status", "payment_date")
    list_filter = ("status", "payment_method", "payment_date")
    search_fields = ("order__id", "transaction_id")


# Registering Schedule model to display in Django Admin
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'day_of_week')  # Columns to display in list view
    search_fields = ('date', 'day_of_week')  # Make these fields searchable
    list_filter = ('day_of_week',)  # Filter by day_of_week in the admin

admin.site.register(Schedule, ScheduleAdmin)

# Registering TimeSlot model to display in Django Admin
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'start_time', 'end_time', 'price', 'status')  # Columns to display
    search_fields = ('schedule__date', 'start_time', 'end_time')  # Searchable fields
    list_filter = ('status', 'schedule__date')  # Filters for status and date

admin.site.register(TimeSlot, TimeSlotAdmin)



@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email')



@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(KeyFigure)
class KeyFigureAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')


