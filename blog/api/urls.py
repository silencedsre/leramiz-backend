from django.urls import path
from .views import CommentListAPIView
app_name = 'blog'
urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list')
]