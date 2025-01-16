from django.db import models

# Create your models here.

class WebPage(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Upload logo image
    facebook_link = models.URLField(max_length=500, blank=True, null=True)  # Facebook URL
    twitter_link = models.URLField(max_length=500, blank=True, null=True)  # Twitter URL
    instagram_link = models.URLField(max_length=500, blank=True, null=True)  # Instagram URL
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)  # LinkedIn URL

    # Metadata
    meta_description = models.CharField(max_length=255, blank=True, null=True)  # SEO meta description
    keywords = models.CharField(max_length=255, blank=True, null=True)  # SEO keywords


    # Status and Configuration
    is_published = models.BooleanField(default=False)  # Publish status
    template_name = models.CharField(max_length=100, blank=True, null=True)  # Optional template choice



class HeroSlide(models.Model):
    # Slide Content
    badge_text = models.CharField(max_length=100, blank=True, null=True)  # Badge text (e.g., "Opening Sale Discount 50%")
    title = models.CharField(max_length=255)  # Slide title
    subtitle = models.CharField(max_length=255, blank=True, null=True)  # Optional subtitle
    description = models.TextField(blank=True, null=True)  # Slide description
    button_label = models.CharField(max_length=50, blank=True, null=True)  # Button text (e.g., "Shop Now")
    button_link = models.URLField(max_length=500, blank=True, null=True)  # Button link

    # Background
    background_image = models.ImageField(upload_to="hero_slides/", blank=True, null=True)  # Slide background image
    background_position = models.CharField(
        max_length=50, 
        choices=[
            ("center", "Center"),
            ("top", "Top"),
            ("bottom", "Bottom"),
            ("left", "Left"),
            ("right", "Right"),
        ], 
        default="center"
    )  # CSS background-position
    background_size = models.CharField(
        max_length=50, 
        choices=[
            ("cover", "Cover"),
            ("contain", "Contain"),
        ], 
        default="cover"
    )  # CSS background-size
    background_repeat = models.BooleanField(default=False)  # Whether background repeats

    # Order and Status
    order = models.PositiveIntegerField(default=0)  # Slide order in the slider
    is_active = models.BooleanField(default=True)  # Whether the slide is active

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Slide creation time
    updated_at = models.DateTimeField(auto_now=True)  # Slide last update time

    class Meta:
        ordering = ['order']  # Slides are ordered by their `order` field

    def __str__(self):
        return self.title




class Banner(models.Model):
    # Content fields
    title = models.CharField(max_length=255)  # Banner title
    description = models.TextField(blank=True, null=True)  # Banner description
    discount_percentage = models.PositiveIntegerField(blank=True, null=True)  # Discount percentage, if applicable
    button_label = models.CharField(max_length=50, blank=True, null=True)  # Button text (e.g., "Shop Now")
    button_link = models.URLField(max_length=500, blank=True, null=True)  # Button link

    # Background customization
    background_image = models.ImageField(upload_to="banners/")  # Background image
    background_position = models.CharField(
        max_length=50,
        choices=[
            ("center", "Center"),
            ("top", "Top"),
            ("bottom", "Bottom"),
            ("left", "Left"),
            ("right", "Right"),
        ],
        default="center",
    )  # CSS background-position
    background_size = models.CharField(
        max_length=50,
        choices=[
            ("cover", "Cover"),
            ("contain", "Contain"),
        ],
        default="cover",
    )  # CSS background-size
    background_repeat = models.BooleanField(default=False)  # Whether background repeats

    # Order and status
    order = models.PositiveIntegerField(default=0)  # Order in the section
    is_active = models.BooleanField(default=True)  # Whether the banner is active

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Created time
    updated_at = models.DateTimeField(auto_now=True)  # Updated time

    class Meta:
        ordering = ['order']  # Order by `order` field in ascending order

    def __str__(self):
        return self.title
