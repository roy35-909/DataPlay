from django.db import models
from user.models import Instructor
import os
# Create your models here.
# Course model
class Course(models.Model):
    instructors = models.ManyToManyField(Instructor)
    course_order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    learn = models.TextField(null=True,blank=True)
    requirements = models.TextField(null=True,blank=True)
    
    image = models.FileField(upload_to="course/thumbnail",null=True,blank=True)
    course_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    content_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    course_price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    content_price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    course_duration = models.IntegerField(default=10)
    course_percentage = models.IntegerField(default=10)

    def __str__(self):
        return self.title

# FileField model
class FileField(models.Model):
    files = models.FileField(upload_to="course/content", max_length=100)

    def __str__(self):
        return f"File : {os.path.basename(self.files.name)}"


class VideoLinks(models.Model):
    topic_name=models.CharField(null=True,blank=True, max_length=255)
    link = models.URLField()
    def __str__(self) -> str:
        return f'{self.topic_name} ===> id: {self.id}'
# CourseContents model
class CourseContents(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    content_order = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    files = models.ManyToManyField(FileField,null=True,blank=True)
    video_link = models.ManyToManyField(VideoLinks,null=True,blank=True)


    class Meta:
        ordering = ['content_order']





    def save(self, *args, **kwargs):
        desired_order = self.content_order
        CourseContents.objects.filter(content_order__gte=desired_order).update(content_order=models.F('content_order') + 1)
        super(CourseContents, self).save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.course}: Content {self.content_order}"