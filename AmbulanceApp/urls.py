from django.contrib import admin
from django.urls import path
from AmbulanceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('ambulance/', views.ambulance, name='ambulance'),
    path('booked_ambulances/', views.booked, name='booked'),
    path('nearby_hospitals/', views.hospitals, name='hospitals'),
    path('services/', views.services, name='services'),
    path('ambulance_register/', views.ambulance_register, name='ambulance_register'),
    path('ambulance_login/', views.ambulance_login, name='ambulance_login'),
    path('booking_request/', views.booking_request, name='booking_request'),
    path('emergency_booking/', views.emergency_booking, name='emergency_booking'),
    path('ambulance_status/', views.ambulance_status, name='ambulance_status'),
    path('driver_profile/', views.driver_profile, name='driver_profile'),
    path('near_hospitals/', views.near_hospitals, name='near_hospitals'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update_profile, name='update_profile'),


]
