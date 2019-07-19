"""leramiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from about.views import index
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', include('about.urls', namespace='about')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('api/', include('blog.api.urls', namespace='comment-api')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('featured-listing/', include('featured_listing.urls', namespace='featured_listing')),
    path('search/', include('search.urls', namespace='search')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)