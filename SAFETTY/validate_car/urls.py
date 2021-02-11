from django.urls import path,include
from validate_car import views

app_name = 'validate_car'

urlpatterns = [
     path('cars/', views.CarListView.as_view(), name='cars'),
     path('drivers/', views.DriverListView.as_view(), name='drivers'),
     path('drivers/<int:pk>', views.DriverDetailView.as_view(), name='driver-detail'),
     path('cars/<int:pk>', views.CarDetailView.as_view(), name='car-detail'),
]
