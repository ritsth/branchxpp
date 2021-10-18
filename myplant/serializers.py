from rest_framework import serializers
from .models import Question,Choice,AddPlant,Posts,Comment,Profile,Notifications
from django.contrib.auth.admin import User
from rest_framework.authtoken.views import Token
import datetime


class QuestionSerializer(serializers.ModelSerializer):
    user =serializers.CharField()
    class Meta:
        model = Question
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = '__all__'



class humiditySerializer(serializers.Serializer):
      humidity = serializers.CharField(default=0)


class nearbyDeviceSerializer(serializers.Serializer):
      nearbyDevices = serializers.CharField(default=0)
      deviceNames= serializers.CharField()
    
class ChoiceSerializer(serializers.ModelSerializer):
    question=serializers.CharField()
    class Meta:
        model = Choice
        fields = '__all__'
        
class AddPlantSerializer(serializers.ModelSerializer):
    user_name2 = serializers.CharField(source='user',read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model =AddPlant
        fields = '__all__'
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_name5 = serializers.CharField(source='user',read_only=True)
    class Meta:
        model =Profile
        fields = '__all__'
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)
    
class PostsSerializer(serializers.ModelSerializer):
    user_name3 = serializers.CharField(source='user',read_only=True)
    type_name = serializers.CharField(source='type',read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Posts
        fields = '__all__'
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)

class CommentSerializer(serializers.ModelSerializer):
    user_name1 = serializers.CharField(source='user',read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','email','password','date_joined',]
 
        extra_kwargs = {'password': {
            'write_only':True,
            'required':True
        }}       
 
 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user