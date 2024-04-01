from django.urls import path
from .views import LoginAPI, add_device, devices_list, update_device, DeviceStatusDetailView,delete_device,add_district,districts_list,update_district,delete_district,taluks_list,add_taluk,update_taluk,delete_taluk,add_village,village_list,update_village,delete_village,customers_list,update_customer,delete_customer,add_customer,add_property_registration,property_registrations_list,update_property_registration,delete_property_registration,add_property_device,property_device_list,update_property_device,delete_property_device,geolocations_by_propertyregistrations,dashboard_data,survey_details_api,TokenGeneratorView


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login-api'),
    path('dashboard/', dashboard_data, name='dashboard_data'),
    path('device/add/', add_device, name='add-device'),
    path('devices/', devices_list, name='devices-list'),
    path('device/update/<int:pk>/', update_device, name='update-device'),
    path('device/delete/<int:pk>/', delete_device, name='delete-device'),
    path('district/add/', add_district, name='add-district'),
    path('districts/', districts_list, name='districts-list'),
    path('district/update/<int:pk>/', update_district, name='update-district'),
    path('district/delete/<int:pk>/', delete_district, name='delete-district'),
    path('taluk/add/', add_taluk, name='add-taluk'),
    path('taluks/', taluks_list, name='taluk-list'),
    path('taluks/<int:district_id>/', taluks_list, name='taluks-list-by-district'),
    path('taluk/update/<int:pk>/', update_taluk, name='update-taluk'),
    path('taluk/delete/<int:pk>/', delete_taluk, name='delete-taluk'),
    path('village/add/', add_village, name='add-village'),
    path('villages/', village_list, name='village-list'),
    path('villages/<int:taluk_id>/', village_list, name='village-list-by-taluks'),
    path('village/update/<int:pk>/', update_village, name='update-village'),
    path('village/delete/<int:pk>/', delete_village, name='delete-village'),
    path('customer/add/', add_customer, name='add-customer'),
    path('customers/', customers_list, name='customers-list'),
    path('customer/update/<int:pk>/', update_customer, name='update-customer'),
    path('customer/delete/<int:pk>/', delete_customer, name='delete-customer'),
    
    path('propertyregistration/add/', add_property_registration, name='add-property-registration'),
    path('propertyregistrations/', property_registrations_list, name='property-registration-list'),
    path('propertyregistration/update/<int:pk>/', update_property_registration, name='update-property-registration'),
    path('propertyregistration/delete/<int:pk>/', delete_property_registration, name='delete-property-registration'),
    path('propertyregistrations/<int:pk>/geolocations', geolocations_by_propertyregistrations, name='geolocations-by-propertyregistrations'),
    
    path('propertydevice/add/', add_property_device, name='add-property-device'),
    path('propertydevices/', property_device_list, name='property-device-list'),
    path('propertydevice/update/<int:pk>/', update_property_device, name='update-property-device'),
    path('propertydevice/delete/<int:pk>/', delete_property_device, name='delete-property-device'),
    path('survey-details/<int:pk>/', survey_details_api, name='survey-details-api'),
    path('api/devicesUpdates/<str:device_id>/', DeviceStatusDetailView.as_view(), name='device-status-detail'),
    path('generate-token/', TokenGeneratorView.as_view(), name='generate_token'),
]