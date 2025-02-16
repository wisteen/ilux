from django.utils import timezone
from django.db.models import Count
from .models import Category, Product, Promotion, PageContent, Wishlist
from webdata.models import HeroSlide, Banner, WebPage
def global_site_data(request):
    """Make site-wide data available globally in templates"""

    categories = Category.objects.all()
    products = Product.objects.select_related('category').prefetch_related('images')[:10]  # Limit to 10 products
    promotions = Promotion.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    banners = Banner.objects.filter(is_active=True).order_by('order')
    web_page = WebPage.objects.filter(is_published=True).first()

    trending_categories = Category.objects.annotate(
        product_count=Count('products')
    ).order_by('-product_count')[:6]  # Top 6 trending categories

    half = len(categories) // 2
    left_categories = categories[:half]
    right_categories = categories[half:]

    popular_products = Product.objects.order_by('-views')[:5]  # Top 5 most viewed products
    latest_products = Product.objects.prefetch_related('images').order_by('-created_at')[:10]  # Latest products

    all_products = Product.objects.all()
    wishlist = []

    if request.user.is_authenticated:
        wishlist_obj, _ = Wishlist.objects.get_or_create(user=request.user)
        wishlist = wishlist_obj.products.values_list('id', flat=True)

    # Page Categories
    pages = {
        "Get to know Us": PageContent.objects.filter(page_type="Get to know Us"),
        "For Consumers": PageContent.objects.filter(page_type="For Consumers"),
        "Become a Drop Shipper": PageContent.objects.filter(page_type="Become a Drop Shipper"),
        "Promo & Deals": PageContent.objects.filter(page_type="Promo & Deals"),
    }

    return {
        'categories': categories,
        'page_category': pages,
        'products': products,
        'promotions': promotions,
        'trending_categories': trending_categories,
        'popular_products': popular_products,
        'latest_products': latest_products,
        'wishlist': wishlist,
        'slides': slides,
        'banners': banners,
        'web_page': web_page,
        'left_categories': left_categories,
        'right_categories': right_categories,
    }
