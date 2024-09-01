from django.db import models
from authentication.models import User
from user.models import Instructor,Students

# Testimonial model
class Testimonial(models.Model):
    order = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    content = models.TextField()
    profile = models.FileField(upload_to='testimonial_profiles', null=True, blank=False)
    prevorg = models.TextField(null=True,blank=False)
    prevrole = models.TextField(null=True,blank=False)
    currorg = models.TextField(null=True,blank=False)
    currrole = models.TextField(null=True, blank=False)
    linkdin = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    video_testimonial_link = models.URLField(null=True, blank=False)
    def __str__(self):
        return self.author
    
