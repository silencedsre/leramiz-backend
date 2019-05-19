from django.urls import path
from .views import FeaturedListingView, FeaturedListingDetail
app_name = 'featured_listing'
urlpatterns = [
    path('', FeaturedListingView.as_view(), name='categories'),
    path('<int:pk>/', FeaturedListingDetail.as_view(), name='detail'),
]