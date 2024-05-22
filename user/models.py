from django.db import models
from authentication.models import User


# Instructor model
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    bio = models.TextField(null=True,blank=True)
    Designation  = models.TextField(null=True,blank=True)
    linkedin = models.CharField(max_length=100, null=True,blank=True)
    profile_pic = models.ImageField(default="default_profile.jpg", upload_to="profiles/instractor")

    def __str__(self):
        return self.user.email
    

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    bio = models.TextField(null=True,blank=True)
    Designation  = models.TextField(null=True,blank=True)
    linkedin = models.CharField(max_length=100, null=True,blank=True)
    profile_pic = models.ImageField(default="default_profile.jpg", upload_to="profiles/mentor")

    def __str__(self):
        return self.user.email
    

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    linkedin = models.CharField(max_length=100, default="..")
    profile_pic = models.ImageField(default="default_profile.jpg", upload_to="profiles/students")

    def __str__(self):
        return self.name