from django.shortcuts import render
from .models import HeroSlide

def hero_slider_view(request):
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    return render(request, "index.html", {"slides": slides})
