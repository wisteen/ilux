from django.contrib import admin
from .models import Banner
from .models import HeroSlide

from .models import WebPage

class WebPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'is_published', 'template_name')
    list_filter = ('is_published',)
    search_fields = ('meta_description', 'keywords')
    fieldsets = (
        ('General Information', {
            'fields': ('logo', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link')
        }),
        ('SEO Metadata', {
            'fields': ('meta_description', 'keywords'),
            'classes': ('collapse',),
        }),
        ('Status and Configuration', {
            'fields': ('is_published', 'template_name'),
        }),
    )
    save_on_top = True

admin.site.register(WebPage, WebPageAdmin)

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'badge_text')
    list_filter = ('is_active', 'created_at')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created_at')


