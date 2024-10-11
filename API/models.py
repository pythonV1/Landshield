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
    respont_frequency = models.IntegerField(default=0)

    device_status = models.BooleanField(default=False)  # BooleanField
    
    def __str__(self):
        return f"{self.device_id} - {self.device_type.name}"

class DeviceStatus(models.Model):
    device_id = models.CharField(max_length=100)
    battery_status = models.CharField(max_length=100, default='')
    device_status = models.BooleanField(default=False)  # BooleanField
    device_log = models.CharField(max_length=100)
    device_lat = models.CharField(max_length=100)
    device_gforce = models.CharField(max_length=100)
    device_movement = models.IntegerField(default=0)
   

class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #area = models.FloatField()  # Assuming area is in square kilometers
    #population_density = models.FloatField()  # Calculated field (population / area)

    def __str__(self):
        return self.name
    
class Taluk(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Village(models.Model):
    name = models.CharField(max_length=100)
    taluk = models.ForeignKey('Taluk', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    user_name = models.CharField(max_length=255)  # Customer's username
    password = models.CharField(max_length=255, default='default_password') 

    def __str__(self):
        return self.name
    


class PropertyRegistration(models.Model):
    property_id = models.CharField(max_length=100)
    property_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    taluk = models.ForeignKey(Taluk, on_delete=models.CASCADE)
    survey_number = models.CharField(max_length=100)
    survey_sub_division = models.CharField(max_length=100)
    patta_number = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    fmb = models.FileField(upload_to='fmb_pdfs')
    def save(self, *args, **kwargs):
        if not self.property_id:
            last_property = PropertyRegistration.objects.order_by('-id').first()
            if last_property:
                last_property_id = int(last_property.property_id)
                self.property_id = str(last_property_id + 1000)
            else:
                # If no PropertyRegistration exists, start from 1000
                self.property_id = '1000'

        super(PropertyRegistration, self).save(*args, **kwargs)

    def __str__(self):
        return self.property_id
       
class Geolocation(models.Model):
    property_registration = models.ForeignKey(PropertyRegistration, related_name='geolocations', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    device_movement = models.IntegerField(default=0)

    def __str__(self):
        return f"Location for {self.property_registration.property_name}"
    
    
class PropertyDevice(models.Model):
    property_id = models.ForeignKey(PropertyRegistration, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, through='PropertyDeviceDevice')
    updated = models.DateField(auto_now=True)  # Add this line
    last_updated = models.DateField(auto_now=True)  # Add this line

class PropertyDeviceDevice(models.Model):
    property_device = models.ForeignKey(PropertyDevice, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)  # Add this line
    # Add other fields as needed

    def __str__(self):
        return f"{self.property_device} - {self.device}"