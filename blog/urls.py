from django.urls import path
from .views import Blog, BlogList, BlogDetail, CommentList
from . import views
app_name = 'blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('<int:pk>', BlogDetail.as_view(), name='detail'),
    path('comment-form/', views.comment_form),
    path('comments/', CommentList.as_view(), name='comments')
]