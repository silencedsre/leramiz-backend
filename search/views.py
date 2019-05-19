from django.views.generic import ListView
from django.db.models import Q
from featured_listing.models import FeaturedListing

# Create your views here.
class SearchListView(ListView):
    model = FeaturedListing
    template_name = "search.html"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs )
        query = self.request.GET.get('q')
        print(query)
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q' or None)
        if query is not None:
            lookups = Q(location__icontains=query) | Q(building_type__icontains=query) | Q(description__icontains=query)
            return FeaturedListing.objects.filter(lookups).distinct()