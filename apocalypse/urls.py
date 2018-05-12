"""apocalypse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('event/', include('booking.urls')),
    path('skirmish/', views.skirmish, name='skirmish'),
    path('under18/', views.under18, name='under18'),
    path('milsim/', views.milsim, name='milsim'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/commandpost', views.commandpost_gallery, name='commandpost_gallery'),
    path('gallery/village', views.village_gallery, name='village_gallery'),
    path('gallery/safezone', views.safezone_gallery, name='safezone_gallery'),
    path('gallery/outlining', views.outlining_gallery, name='outlining_gallery'),
    path('gallery/trenches', views.trenches_gallery, name='trenches_gallery'),
    path('gallery/under18', views.under18_gallery, name='under18_gallery'),
    path('bookings/', views.bookings, name='bookings'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:blog_id>/', views.eachblog, name='eachblog'),
    path('admin/addevent/', views.addevent, name='addevent'),
    path('admin/addblog/', views.addblog, name='addblog'),
    path('admin/uploadpic/', views.uploadpic, name='uploadpic'),
]
