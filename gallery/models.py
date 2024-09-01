from django.db import models
from course.models import Course

class WorkShopGallery(models.Model):
    image = models.FileField(blank=False, upload_to='workshopgallery')
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    venue = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'ID ==> {self.id}, Venue ==> {self.venue}'
    

class CourseFeedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    photo = models.FileField(blank=False, upload_to='FeedBackPhoto')
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    linkedin = models.URLField()
    content = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f'ID ==> {self.id}, Name ==> {self.name}, Course ==> {self.course.title}'
    


class OurTeam(models.Model):
    photo = models.FileField(upload_to='OurTeam')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    


    
