from django.shortcuts import render
from .models import Question,Choice,AddPlant,Posts,Comment,Profile,Notifications
from .serializers import QuestionSerializer,UserSerializer,NotificationsSerializer,ChoiceSerializer,AddPlantSerializer,humiditySerializer,PostsSerializer,CommentSerializer,ProfileSerializer,nearbyDeviceSerializer
from rest_framework import viewsets
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.admin import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.utils import timezone
import datetime
#import bluetooth
#import time


from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    now=timezone.now()
    later=timezone.now()-datetime.timedelta(days=2)
    queryset=Question.objects.filter(pub_date__range=(later,now)).order_by('-pub_date')


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    now=timezone.now()
    later=timezone.now()-datetime.timedelta(days=2)
    later_later=timezone.now()-datetime.timedelta(days=4)
    queryset=Question.objects.filter(pub_date__range=(later_later,later)).order_by('-pub_date')

class AddPlantViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class= AddPlantSerializer
    queryset=AddPlant.objects.all()
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class PostsLaterViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class= PostsSerializer
    later=timezone.now()+datetime.timedelta(hours=6)-datetime.timedelta(days=4)
    later_later=timezone.now()-datetime.timedelta(days=50)
    queryset=Posts.objects.filter(pub_date__range=(later_later,later)).order_by('-pub_date')

class PostsNowViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class=PostsSerializer
    now=timezone.now()+datetime.timedelta(hours=6)
    later=now-datetime.timedelta(days=5)
    queryset=Posts.objects.all().filter(pub_date__range=(later,now)).order_by('-pub_date')

class AllPostsViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class=PostsSerializer
    queryset=Posts.objects.all().order_by('-pub_date')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


x=0
y=0
#nearby_devices=bluetooth.discover_devices()
#devices_names=bluetooth.discover_devices(lookup_names=True)
class nearbyBluetoothDevice:
    def __init__(self,nearbyDevices,deviceNames):
        self.nearbyDevices=nearbyDevices
        self.deviceNames=deviceNames

class nearbyDevicesViewSet(viewsets.ViewSet):
    
    def list(self,request):
        serializer=nearbyDeviceSerializer(nearbyBluetoothDevice(nearbyDevices=nearby_devices[x],
                                                                deviceNames=devices_names[y][1]))
        return Response(serializer.data)
    def create(self,request):
        global x
        global y
        x=x+1
        y=y+1
        if (x >= len(nearby_devices)):
            x=0        
        if (y >= len(nearby_devices)):
            y=0
        serializer=nearbyDeviceSerializer(nearbyBluetoothDevice(nearbyDevices=nearby_devices[x],
                                                                deviceNames=devices_names[y][1]))
        return Response(serializer.data)

class humidityStat:
    def __init__(self,humidity):
        self.humidity = humidity
   

#s=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=1
size=1024
class humidityViewSet(viewsets.ViewSet):
    def list(self,request):
        serializer=nearbyDeviceSerializer(nearbyBluetoothDevice(nearbyDevices=nearby_devices,
                                                                deviceNames=devices_names))
        return Response(serializer.data)

    def retrieve(self,request,pk):
        add=AddPlant.objects.values_list('device',flat=True).get(pk=pk)
        #s.connect((add,port))
        #data=s.recv(size).decode("utf-8")
        serializer=humiditySerializer(humidityStat(humidity=data))
        return Response(serializer.data)


    def update(self,request,pk):
        data=s.recv(size).decode("utf-8")
        serializer=humiditySerializer(humidityStat(humidity=data))
        return Response(serializer.data)
   


class ProfileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]


    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
