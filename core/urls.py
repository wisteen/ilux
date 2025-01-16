from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as form_validation
from . import views
from account.views import register_user

urlpatterns = [
    path('', views.homepage, name='home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('get-header-cart-data/', views.get_header_cart_data, name='get_header_cart_data'),
    # path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/details/', views.get_product_details, name='get_product_details'),
    path('cart/data/', views.get_cart_data, name='get_cart_data'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/update/<int:item_id>/', views.update_cart_item_quantity, name='update_cart_item'),
    path("wishlist/toggle/<int:product_id>/", views.toggle_wishlist, name="toggle_wishlist"),
    path("wishlist/count/", views.wishlist_count, name="wishlist_count"),

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/review/', views.submit_review, name='submit_review'),


    path("get-wishlist/", views.get_wishlist, name="get_wishlist"),
    path("wishlist/", views.wishlist, name="add_to_wishlist"),
    path("remove-from-wishlist/", views.remove_from_wishlist, name="remove_from_wishlist"),


    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/<int:order_id>/', views.checkout_view, name='order-details'),
    path('add-address/', views.add_address, name='add_address'),
    path('address/delete/<int:address_id>/', views.delete_address, name='delete_address'),

    path('order-success/<int:order_id>/', views.order_success_view, name='order_success'),
    path('order/<int:order_id>/payment/', views.make_payment, name='make_payment'),
    path('payment/callback/<int:order_id>/', views.payment_callback, name='payment_callback'),

    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('category/<slug:slug>/', views.category_detail_view, name='category_detail'),
    path('register/', register_user, name='register_user'),

    path('products/', views.products_view, name='products'),
    path('filter/', views.filter_page, name='filter_page'),
    # path('payment/<int:order_id>/', views.payment_page, name='payment_page'),

]


