from django.db import models

from authentication.models import User


# Instructor model
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    bio = models.TextField(null=True,blank=False)
    Designation  = models.TextField(null=True,blank=False)
    linkedin = models.URLField(max_length=100, null=True,blank=True)
    profile_pic = models.FileField(default="default_profile.jpg", upload_to="profiles/instractor")
    education = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return self.user.email
    

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    bio = models.TextField(null=True,blank=True)
    Designation  = models.TextField(null=True,blank=True)
    linkedin = models.URLField(max_length=100, null=True,blank=True)
    profile_pic = models.FileField(default="default_profile.jpg", upload_to="profiles/mentor")
    education = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return self.user.email
    

class Students(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True)
    linkedin = models.URLField(max_length=100, null=True,blank=True)
    profile_pic = models.FileField(default="default_profile.jpg", upload_to="profiles/students", null=True,blank=True) #File Field For uploade Svg, jpg, png, jpeg. 
    mobile_no = models.CharField(max_length=25, null=True,blank=True)
    what_are_you_currently_doing = models.CharField(max_length=100,null=True,blank=True)
    college_name = models.CharField(max_length=255,null=True,blank=True)
    highest_degree_of_study = models.CharField(max_length=255,null=True,blank=True)
    year_of_study = models.IntegerField(null=True,blank=True)
    home_town_city = models.CharField(max_length=255,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    how_did_you_find_us = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.user.first_name