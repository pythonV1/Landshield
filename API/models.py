from django.db import models

class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Device(models.Model):
    device_id = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)  # ForeignKey to DeviceType model
    battery_status = models.CharField(max_length=100, default='')
    device_status = models.BooleanField(default=False)  # BooleanField
    
    def __str__(self):
        return f"{self.device_id} - {self.device_type.name}"
