from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_part_list, name='car_part_list'),
    path('edit/<int:pk>/', views.edit_car_part, name='edit_car_part'),
    path('delete/<int:pk>/', views.delete_car_part, name='delete_car_part'),
]
