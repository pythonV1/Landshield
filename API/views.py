from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Device,DeviceStatus, District,Taluk,Village,Customer,PropertyRegistration,PropertyDevice,Geolocation,PropertyDeviceDevice
from .serializers import DeviceSerializer,DeviceStatusSerializer,DistrictSerializer,TalukSerializer,VillageSerializer,CustomerSerializer,PropertyRegistrationSerializer,GeolocationSerializer,PropertyDeviceSerializer,PropertyDeviceDeviceSerializer
import json
from json.decoder import JSONDecodeError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
import hashlib

def generate_token():
    # Generate a token using a unique identifier (e.g., UUID)
    unique_identifier = 'your_unique_identifier'  # You can use any unique identifier here
    token = hashlib.sha256(unique_identifier.encode()).hexdigest()
    return token

@method_decorator(csrf_exempt, name='dispatch')
class TokenGeneratorView(View):
    def get(self, request, *args, **kwargs):
        # Generate a token
        auth_token = generate_token()

        # Return the token as part of the JSON response
        return JsonResponse({'token': auth_token})

@api_view(['GET'])
def devices_list(request):
    devices = Device.objects.all()
    data = []
    for device in devices:
        device_data = {
            'tab_id': device.id,
            'device_id': device.device_id,
            'device_type': device.device_type.name,  # Assuming 'device_type' is a ForeignKey to your DeviceType model
            'device_type_id': device.device_type.id,
            'battery_status': device.battery_status,
            'device_status': device.device_status
        }
        data.append(device_data)
    return Response(data)

def devices_list_demo(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def device_status_detail_view(request):
    if request.method == 'POST':
        try:
            # Extract form data from the request
            print("hello")
            device_id = request.POST.get('device_id')
            # Check if device_id is None or not
            if device_id is not None:
                # Device ID is present, proceed with processing
                # Your code here
                pass
            else:
                # Device ID is missing, return an error response
                return JsonResponse({"error": "Missing 'device_id' field in form data"}, status=400)
        except Exception as e:
            # Return an error response for any exceptions
            return JsonResponse({"error": f"Error occurred while processing the request: {str(e)}"}, status=500)


@api_view(['POST'])
@csrf_exempt
def device_status_detail_view666(request):
    if request.method == 'POST':
        try:
            # Extract form data from the 
            print("hello")
            device_id = request.POST['device_id']

            # print(device_id)
            # battery_status = request.POST.get('battery_status')
            # device_status = request.POST.get('device_status')
            # device_log = request.POST.get('device_log')
            # device_lat = request.POST.get('device_lat')
            # device_gforce = request.POST.get('device_gforce')
            
            # # Create a new DeviceStatus object
            # device_status_obj = DeviceStatus.objects.create(
            #     device_id=device_id,
            #     battery_status=battery_status,
            #     device_status=device_status,
            #     device_log=device_log,
            #     device_lat=device_lat,
            #     device_gforce=device_gforce
            # )
            
            # Return a success response
            return JsonResponse({"detail": f"Device status created for device ."}, status=201)
        
        except:
            # Return an error response for any exceptions
            return JsonResponse({"error": f"Error occurred while processing the requestssssssssssss "}, status=500)


def device_status_detail_view___(request):
    if request.method == 'POST':
        try:
            # Extract JSON data from the request body
            request_data = json.loads(request.body)
            device_id = request_data.get('device_id')
            battery_status = request_data.get('battery_status')
            device_status = request_data.get('device_status')
            device_log = request_data.get('device_log')
            device_lat = request_data.get('device_lat')
            device_gforce = request_data.get('device_gforce')
            
            # Create a new DeviceStatus object
            device_status_obj = DeviceStatus.objects.create(
                device_id=device_id,
                battery_status=battery_status,
                device_status=device_status,
                device_log=device_log,
                device_lat=device_lat,
                device_gforce=device_gforce
            )
            
            # Return a success response
            return JsonResponse({"detail": f"Device status created for device {device_id}."}, status=201)
        
        except JSONDecodeError:
            # Return an error response for invalid JSON data
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class DeviceStatusDetailView(View):
    def post(self, request,  *args, **kwargs):
        # Extract JSON data from the request body
        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)
        device_id = request_data.get('battery_status', device_status.battery_status)
        # Check if a DeviceStatus object with the given device_id exists
        device_status, created = DeviceStatus.objects.get_or_create(device_id=device_id)

        # Update the device status attributes
        device_status.battery_status = request_data.get('battery_status', device_status.battery_status)
        device_status.device_status = request_data.get('device_status', device_status.device_status)
        device_status.device_log = request_data.get('device_log', device_status.device_log)
        device_status.device_lat = request_data.get('device_lat', device_status.device_lat)
        device_status.device_gforce = request_data.get('device_gforce', device_status.device_gforce)

        # Save the device status object
        device_status.save()

        # Return a JSON response
        return JsonResponse({"detail": f"Device status updated for device {device_id}."})

@api_view(['PUT', 'PATCH'])
def update_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    serializer = DeviceSerializer(device, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def districts_list(request):
    if request.method == 'GET':
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_district(request):
    serializer = DistrictSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_district(request, pk):
    district = get_object_or_404(District, pk=pk)
    serializer = DistrictSerializer(instance=district, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_district(request, pk):
    district = get_object_or_404(District, pk=pk)
    district.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def taluks_list(request, district_id=None):
    if request.method == 'GET':
        # Check if district_id is provided
        if district_id is not None:
            # Filter taluks based on the district ID
            taluks = Taluk.objects.filter(district=district_id)
        else:
            # Get all taluks
            taluks = Taluk.objects.all()

        serializer = TalukSerializer(taluks, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_taluk(request):
    serializer = TalukSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_taluk(request, pk):
    taluk = get_object_or_404(Taluk, pk=pk)
    serializer = TalukSerializer(instance=taluk, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_taluk(request, pk):
    taluk = get_object_or_404(Taluk, pk=pk)
    taluk.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def village_list(request, taluk_id=None):
    if request.method == 'GET':
        if taluk_id is not None:
            
            villages = Village.objects.filter(taluk=taluk_id)
        else:
             villages = Village.objects.all()
            
        serializer = VillageSerializer(villages, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_village(request):
    serializer = VillageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_village(request, pk):
    village = get_object_or_404(Village, pk=pk)
    serializer = VillageSerializer(instance=village, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_village(request, pk):
    village = get_object_or_404(Village, pk=pk)
    village.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def customers_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_customer(request, pk):
    village = get_object_or_404(Customer, pk=pk)
    serializer = CustomerSerializer(instance=village, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, pk):
    village = get_object_or_404(Customer, pk=pk)
    village.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def property_registrations_list(request):
    if request.method == 'GET':
        propertyRegistrations = PropertyRegistration.objects.all()
        serializer = PropertyRegistrationSerializer(propertyRegistrations, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@parser_classes([MultiPartParser])
def add_property_registration(request):
    serializer = PropertyRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        property_registration = serializer.save()

        # Add geolocations
        geolocations_data_str_list = request.data.getlist('geolocations')  # Assuming geolocations is a list
        for geolocation_data_str in geolocations_data_str_list:
            try:
                geolocation_data = json.loads(geolocation_data_str)
                geolocation_serializer = GeolocationSerializer(data=geolocation_data)
                if geolocation_serializer.is_valid():
                    geolocation_serializer.save(property_registration=property_registration)
                else:
                    return Response(geolocation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except JSONDecodeError as e:
                return Response({'error': 'Invalid JSON format in geolocations'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@parser_classes([MultiPartParser])
def update_property_registration(request, pk):
    # Handling geolocations data
    geolocations_data_str_list = request.data.getlist('geolocations')
    for geolocation_data_str in geolocations_data_str_list:
        try:
            geolocation_data = json.loads(geolocation_data_str)
            # Further processing of geolocation_data if needed
        except JSONDecodeError as e:
            print("Error decoding JSON:", e)
            # Handle the error as needed

    # Fetching the property registration instance
    property_registration = get_object_or_404(PropertyRegistration, pk=pk)
    
    # Updating the property registration instance
    property_registration_serializer = PropertyRegistrationSerializer(instance=property_registration, data=request.data, partial=True)
    
    if property_registration_serializer.is_valid():
        property_registration_serializer.save()
        property_registration.geolocations.all().delete()
        # Update or create geolocations
        #geolocations_data = request.data.get('geolocations')
        
        # Add geolocations
        geolocations_data_str_list = request.data.getlist('geolocations')  # Assuming geolocations is a list
        for geolocation_data_str in geolocations_data_str_list:
            try:
                geolocation_data = json.loads(geolocation_data_str)
                geolocation_serializer = GeolocationSerializer(data=geolocation_data)
                if geolocation_serializer.is_valid():
                    geolocation_serializer.save(property_registration=property_registration)
                else:
                    return Response(geolocation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except JSONDecodeError as e:
                return Response({'error': 'Invalid JSON format in geolocations'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(property_registration_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(property_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET'])
def geolocations_by_propertyregistrations(request, pk):
    try:
        geolocations = Geolocation.objects.filter(property_registration=pk)
        serializer = GeolocationSerializer(geolocations, many=True)
        return Response(serializer.data)
    except Geolocation.DoesNotExist:
        return Response(status=404)
   

   
@api_view(['DELETE'])
def delete_property_registration(request, pk):
    propertyregistration = get_object_or_404(PropertyRegistration, pk=pk)
    propertyregistration.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def property_device_list(request):
    if request.method == 'GET':
        # Fetch all PropertyDevice instances
        property_devices = PropertyDevice.objects.all()
        
        # Serialize the PropertyDevice instances
        serializer = PropertyDeviceSerializer(property_devices, many=True)
        
        # Retrieve related data from PropertyDeviceDevice and add it to the serialized output
        for obj in serializer.data:
            property_device_id = obj['id']  # Assuming id is the primary key of PropertyDevice
            
            # Fetch related PropertyDeviceDevice instances for this PropertyDevice
            property_device_devices = PropertyDeviceDevice.objects.filter(property_device=property_device_id)
            
            # Serialize the related PropertyDeviceDevice instances
            property_device_devices_data = PropertyDeviceDeviceSerializer(property_device_devices, many=True).data
            
            # Add the serialized PropertyDeviceDevice data to the PropertyDevice serialization
            obj['propertydevice_devices'] = property_device_devices_data
        
        return Response(serializer.data)



@api_view(['POST'])
def add_property_device(request):
    # Deserialize PropertyDevice data
    serializer = PropertyDeviceSerializer(data=request.data)
    if serializer.is_valid():
        # Save PropertyDevice instance
        property_device_instance = serializer.save()
        inserted_id = property_device_instance.id
        # Get propertydeviceList data
        property_device_devices_data = request.data.get('propertydeviceList', [])

        # Create PropertyDeviceDevice instances
        for device_data in property_device_devices_data:
            # Assign PropertyDevice instance to property_device field
            device_data['property_device'] = inserted_id
            #print(device_data)
            
            #Serialize and save PropertyDeviceDevice instance
            device_serializer = PropertyDeviceDeviceSerializer(data=device_data)
            if device_serializer.is_valid():
                device_serializer.save()
            else:
                return Response(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Return errors if PropertyDevice data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def dashboard_data(request):
    # Get total number of customers
    total_customers = Customer.objects.count()
    
    # Get total number of devices
    total_devices = Device.objects.count()
    
    # Get count of active devices
    active_devices = Device.objects.filter(device_status=True).count()
    
    # Get count of inactive devices
    inactive_devices = Device.objects.filter(device_status=False).count()
    
    # Prepare data to return
    data = {
        'total_customers': total_customers,
        'total_devices': total_devices,
        'active_devices': active_devices,
        'inactive_devices': inactive_devices
    }
    
    # Return data in JSON format
    return Response(data)
   
@api_view(['POST'])
def update_property_device(request, pk):
    try:
        # Retrieve the PropertyDevice instance by its primary key (pk)
        property_device_instance = PropertyDevice.objects.get(pk=pk)
    except PropertyDevice.DoesNotExist:
        # Return 404 Not Found response if PropertyDevice instance does not exist
        return Response({'error': 'PropertyDevice does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Deserialize the updated PropertyDevice data
    serializer = PropertyDeviceSerializer(property_device_instance, data=request.data)
    if serializer.is_valid():
        # Save the updated PropertyDevice instance
        updated_property_device_instance = serializer.save()
        
        # Get propertydeviceList data
        property_device_devices_data = request.data.get('propertydeviceList', [])
        
        # Delete existing PropertyDeviceDevice instances related to the updated PropertyDevice instance
        property_device_instance.propertydevicedevice_set.all().delete()
        
        # Create new PropertyDeviceDevice instances
        for device_data in property_device_devices_data:
            # Assign the updated PropertyDevice instance to property_device field
            device_data['property_device'] = updated_property_device_instance.id
            
            # Serialize and save the new PropertyDeviceDevice instance
            device_serializer = PropertyDeviceDeviceSerializer(data=device_data)
            if device_serializer.is_valid():
                device_serializer.save()
            else:
                # Return errors if PropertyDeviceDevice data is invalid
                return Response(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Return the serialized updated PropertyDevice instance with a status of 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # Return errors if PropertyDevice data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def delete_property_device(request, pk):
    propertydevice = get_object_or_404(PropertyDevice, pk=pk)
    propertydevice.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def survey_details_api(request, pk):
    try:
        # Retrieve the PropertyDevice object based on the provided property_device_id
        property_device = PropertyDevice.objects.get(id=pk)
        property_registration = property_device.property_id
        customer_name = property_device.customer_id.name if property_device.customer_id else None

        # Extract survey details from the related PropertyRegistration object
        survey_details = {
            'property_name': property_registration.property_name,
            'survey_number': property_device.property_id.survey_number,
            'survey_sub_division': property_device.property_id.survey_sub_division,
            'patta_number': property_device.property_id.patta_number,
            'area': property_device.property_id.area,
            'taluk': property_device.property_id.taluk.name,
            'village': property_device.property_id.village.name,
            'fmb_url': property_device.property_id.fmb.url,  # Assuming fmb is a FileField
            'customer_name': customer_name,
            'district_name': property_registration.district.name,
            'village_name': property_registration.village.name,
            'taluk_name': property_registration.taluk.name,
            
            
        }
        
        # Retrieve related devices from PropertyDeviceDevice model
        devices = PropertyDeviceDevice.objects.filter(property_device=property_device)
        device_info = []
        for device in devices:
            device_info.append({
                'device_id': device.device.device_id,
                'battery_status': device.device.battery_status,
                'device_status': device.device.device_status,
                       # Add geolocation details
                'latitude': device.geolocation.latitude,
                'longitude': device.geolocation.longitude,
                # Add other fields as needed
                'last_updated': device.last_updated,
                # Add other fields from Device model as needed
            })
        
        # Combine survey details and device information
        response_data = {
            'survey_details': survey_details,
            'devices': device_info,
            #'devices_devices': devices
            
        }
        
        return JsonResponse(response_data, status=200)
    except PropertyDevice.DoesNotExist:
        return JsonResponse({'error': 'PropertyDevice not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # User authentication successful
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({'message': 'Login successful', 'token': token,'customerName':user.first_name,'address':user.last_name}, status=status.HTTP_200_OK)
        else:
            # Invalid credentials
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def my_view(request):
    active_device_types = DeviceType.objects.filter(status=True)
    return render(request, 'API/device_type_template.html', {'active_device_types': active_device_types})


