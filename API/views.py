from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Device
from .serializers import DeviceSerializer

@api_view(['GET'])
def devices_list(request):
    devices = Device.objects.all()
    data = []
    for device in devices:
        device_data = {
            'tab_id': device.id,
            'device_id': device.device_id,
            'device_type': device.device_type.name,  # Assuming 'device_type' is a ForeignKey to your DeviceType model
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


class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # User authentication successful
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # Invalid credentials
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def my_view(request):
    active_device_types = DeviceType.objects.filter(status=True)
    return render(request, 'API/device_type_template.html', {'active_device_types': active_device_types})