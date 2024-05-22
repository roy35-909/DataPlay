from django.db import models
from authentication.models import User
from user.models import Instructor,Students

# Testimonial model
class Testimonial(models.Model):
    order = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    content = models.TextField()
    profile = models.ImageField(upload_to='testimonial_profiles', null=True,blank=True)
    prevorg = models.TextField(null=True,blank=True)
    prevrole = models.TextField(null=True,blank=True)
    currorg = models.TextField(null=True,blank=True)
    currrole = models.TextField(null=True, blank=True)
    linkdin = models.CharField(max_length=100, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
