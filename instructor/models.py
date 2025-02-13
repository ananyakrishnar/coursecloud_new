from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from embed_video.fields import EmbedVideoField

class User(AbstractUser):

    ROLE_OPTIONS=(
        ("student","student"),
        ("instructor","instructor")
    )

    role=models.CharField(max_length=20,choices=ROLE_OPTIONS,default="student")

class InstructorProfile(models.Model):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    expertise=models.CharField(max_length=200,null=True)

    picture=models.ImageField(upload_to="profilepics",null=True,blank=True,default="profilepics/default.png")

    description=models.CharField(max_length=200,null=True)

from django.db.models.signals import post_save

def create_instructor_profile(sender,instance,created,**kwargs):

    if created and instance.role=="instructor":

        InstructorProfile.objects.create(owner=instance)

post_save.connect(create_instructor_profile,User)

class Catagory(models.Model):

    name=models.CharField(max_length=200,unique=True)

    def __str__(self):

        return self.name
    
class Course(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    price=models.DecimalField(decimal_places=2,max_digits=5)

    owner=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="courses",null=True)

    is_free=models.BooleanField(default=False)

    picture=models.ImageField(upload_to="courseimages",null=True,blank=True,default="courseimages/default.png")

    thumbnail=EmbedVideoField()

    catagory_objects=models.ManyToManyField(Catagory)

    created_at=models.DateTimeField(auto_now_add=True)

    uploaded_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



    

