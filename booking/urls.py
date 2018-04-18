from django.urls import path

from booking import views

urlpatterns = [
    path('', views.events, name='event'),
    path('<str:event_id>/', views.dates, name='dates'),

]
