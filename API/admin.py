from django.contrib import admin
from .models import Device, DeviceType

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'get_device_type', 'device_status', 'battery_status')
    list_editable = ('battery_status', 'device_status')  # Fields that can be edited directly in the admin list view
    list_display_links = ('device_id',)  # Make the device_id field clickable for editing

    def get_device_type(self, obj):
        return obj.device_type.name
    get_device_type.short_description = 'Device Type'


# Register the Device model with the admin site
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType)
