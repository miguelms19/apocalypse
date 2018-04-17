from django.urls import path

from booking import views


urlpatterns = [
    path('', views.events, name='event'),

]
