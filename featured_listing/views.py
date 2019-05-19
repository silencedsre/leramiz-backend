from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import FeaturedListing

# Create your views here.
class FeaturedListingView(ListView):
    model = FeaturedListing
    template_name = "featured_listing/catagories.html"

class FeaturedListingDetail(DetailView):
    model = FeaturedListing
    template_name = "featured_listing/category_details.html"
