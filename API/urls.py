from django.urls import path
from .views import LoginAPI, add_device, devices_list, update_device, delete_device


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login-api'),
    path('device/add/', add_device, name='add-device'),
    path('devices/', devices_list, name='devices-list'),
    path('device/<int:pk>/', update_device, name='update-device'),
    path('device/delete/<int:pk>/', delete_device, name='delete-device'),
]