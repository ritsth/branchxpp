from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Notifications(models.Model):
    list=models.CharField(max_length=200)
    def __str__(self):
       return self.list

class AddPlant(models.Model):
    name_text=models.CharField(max_length=200)
    type_text=models.CharField(max_length=200)
    plant_img=models.ImageField(default="plant_img")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,editable=False,related_name='user_name2')
    pub_date = models.DateTimeField('Date published',default=timezone.now,editable=False)
    device=models.CharField(max_length=200,default="no devices in range")
    def __str__(self):
          return self.type_text
 
class Posts(models.Model):

      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,editable=False,related_name='user_name3' )
      type= models.ForeignKey(AddPlant ,on_delete=models.CASCADE,related_name='type_name')
      status=models.CharField(max_length=1200,default=" ")
      post_img=models.ImageField(default="post_img")
      pub_date = models.DateTimeField('Date published',default=timezone.now,editable=False)

      def __str__(self):
          return self.status

class Comment(models.Model):
    post=models.ForeignKey(Posts, on_delete=models.CASCADE, null=True,editable=True,related_name='related_post' )
    comment_text=models.CharField(max_length=1200)
    pub_date = models.DateTimeField('Date published',default=timezone.now,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,editable=False,related_name='user_name1' )

class Question(models.Model):
    d=datetime.datetime.now()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published',default=timezone.now,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,editable=True,related_name='user_name4')
    added_by= models.CharField(max_length=200)
    
    def __str__(self):
       return self.question_text
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=5)<=self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question ,on_delete=models.CASCADE,related_name='question')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
       return self.choice_text


class Profile(models.Model):
    Profile_photo=models.ImageField(default="d")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,editable=True,related_name='user_name5')
    def __str__(self):
        return self.user.username
