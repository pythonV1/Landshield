# serializers.py

from rest_framework import serializers
from .models import Device,DeviceStatus,District,Taluk,Village,Customer,PropertyRegistration,Geolocation,PropertyDevice,PropertyDeviceDevice





class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = ['id', 'device_id', 'battery_status', 'device_status', 'device_log', 'device_lat', 'device_gforce']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'device_type', 'batch_id','mac_id','device_status']
        
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id','name']
        
class TalukSerializer(serializers.ModelSerializer):
    district_name = serializers.SerializerMethodField()

    class Meta:
        model = Taluk
        fields = ['id', 'name', 'district', 'district_name']

    def get_district_name(self, obj):
        return obj.district.name if obj.district else None
    
class VillageSerializer(serializers.ModelSerializer):
    district_name = serializers.SerializerMethodField()
    taluk_name = serializers.SerializerMethodField()


    class Meta:
        model = Village
        fields = ['id', 'name', 'district', 'district_name', 'taluk', 'taluk_name']

    def get_district_name(self, obj):
        return obj.district.name if obj.district else None
    def get_taluk_name(self, obj):
        return obj.taluk.name if obj.taluk else None
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email','mobile_number','address','aadhar_number']
        
class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['id', 'latitude', 'longitude']
    
class PropertyRegistrationSerializer(serializers.ModelSerializer):
    
    district_name = serializers.SerializerMethodField()
    taluk_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()
    geolocations= GeolocationSerializer(many=True, read_only=True)  # Nested serializer for geolocations

    class Meta:
        model = PropertyRegistration
        fields = ['id', 'property_name','district', 'district_name', 'taluk', 'taluk_name','village','village_name','survey_number','survey_sub_division','patta_number','area','fmb', 'geolocations']
         
    def get_district_name(self, obj):
        return obj.district.name if obj.district else None
    def get_taluk_name(self, obj):
        return obj.taluk.name if obj.taluk else None
    def get_village_name(self, obj):
        return obj.village.name if obj.village else None
    
class PropertyDeviceDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDeviceDevice
        fields = ['id', 'geolocation', 'device', 'property_device']
        # Add 'property_device' to the fields list
        # Explicitly set 'property_device' field to accept nested representations
        # extra_kwargs = {
        #     'property_device': {'write_only': True}
        # }

class PropertyDeviceSerializer(serializers.ModelSerializer):
    
    property_name = serializers.SerializerMethodField()
    survey_number = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    customer_mobile = serializers.SerializerMethodField()
    district_name = serializers.SerializerMethodField()
    taluk_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()
    device_names = serializers.SerializerMethodField()  # Change this field name to match the method name
    device_count = serializers.SerializerMethodField()
    devices_info = serializers.SerializerMethodField()

    propertydevice_devices = PropertyDeviceDeviceSerializer(many=True, read_only=True)  

    class Meta:
        model = PropertyDevice
        fields = ['id', 'property_id', 'property_name','survey_number', 'customer_id', 'customer_name', 'customer_mobile', 'taluk_name','district_name', 'village_name', 'device_names',  'device_count', 'devices_info','last_updated','propertydevice_devices']
    
    def get_property_name(self, obj):
        return obj.property_id.property_name if obj.property_id else None
    def get_survey_number(self, obj):
        return obj.property_id.survey_number if obj.property_id else None
     
    def get_customer_name(self, obj):
        try:
            return obj.customer_id.name if obj.customer_id else None
        except AttributeError:
            return None    
    def get_customer_mobile(self, obj):
        return obj.customer_id.mobile_number if obj.customer_id else None
        
    def get_district_name(self, obj):
        return obj.property_id.district.name if obj.property_id else None
    
    def get_taluk_name(self, obj):
        return obj.property_id.taluk.name if obj.property_id else None
    
    def get_village_name(self, obj):
        try:
            return obj.property_id.village.name if obj.property_id and obj.property_id.village else None
        except AttributeError:
            return None


    def get_device_names(self, obj):
        return [device.device_id for device in obj.devices.all()]
    
    def get_device_count(self, obj):
        return obj.devices.count()
    
    def get_devices_info(self, obj):
        devices_info = []
        for device in obj.devices.all():
            devices_info.append({
                'device_id': device.id,
                'device_name': device.device_id,
                # Add other device information fields here as needed
            })
        return devices_info


class PropertyDeviceDeviceSerializerInfo(serializers.ModelSerializer):
    # Define nested serializers for related models
    property_registration = serializers.SerializerMethodField()

    class Meta:
        model = PropertyDeviceDevice
        fields = ['property_device', 'device', 'geolocation', 'last_updated', 'property_registration']

    def get_property_registration1(self, obj):
        # Fetch survey information associated with the property device
        property_registration = PropertyRegistration.objects.get(property_id=obj.property_device.property_id_id)
        return {
            'survey_number': property_registration.survey_number,
            'survey_sub_division': property_registration.survey_sub_division,
            'patta_number': property_registration.patta_number,
            'area': property_registration.area,
            'taluk': property_registration.taluk.name,
            'village': property_registration.village.name,
            'fmb': property_registration.fmb.url  # Assuming you want to include the FMB URL
        }
   


