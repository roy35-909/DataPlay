import os

from django.db import models

from user.models import Instructor
from authentication.models import User
import os

from django.db import models

from user.models import Instructor


# Create your models here.
# Course model
class Course(models.Model):
    instructors = models.ManyToManyField(Instructor)
    course_order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255,null=True,blank=False)
    description = models.TextField(null=True,blank=False)
    learn = models.TextField(null=True,blank=False)
    requirements = models.TextField(null=True,blank=False)
    
    image = models.FileField(upload_to="course/thumbnail",null=True,blank=False)
    course_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    content_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    course_price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    content_price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=2)
    course_duration = models.IntegerField(default=10)
    course_percentage = models.IntegerField(default=10)

    def __str__(self):
        return self.title


class RegisterCourse(models.Model):
    class Meta:
        verbose_name = "AddStudent"
        verbose_name_plural = "AddStudents"
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fee = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Student Email: {self.user.email} Purchased :{self.course.title}'



# FileField model
class FileField(models.Model):
    files = models.FileField(upload_to="course/content", max_length=100)

    def __str__(self):
        return f"File : {os.path.basename(self.files.name)}"


class VideoLinks(models.Model):
    topic_name=models.CharField(null=True,blank=False, max_length=255)
    photo = models.FileField(upload_to="course/thumbnail/videothumbnail",null=True,blank=True)
    link = models.URLField()
    def __str__(self) -> str:
        return f'{self.topic_name} ===> id: {self.id}'
    
class GoogleDriveLinks(models.Model):
    topic_name=models.CharField(null=True,blank=False, max_length=255)
    photo = models.FileField(upload_to="course/thumbnail/filesthumbnail",null=True,blank=True)
    link = models.URLField()
    def __str__(self) -> str:
        return f'{self.topic_name} ===> id: {self.id}'

# CourseContents model
class CourseContents(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    content_order = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=False)
    files = models.ManyToManyField(FileField,null=True,blank=True)
    video_link = models.ManyToManyField(VideoLinks,null=True,blank=True)
    google_drive_link = models.ManyToManyField(GoogleDriveLinks, null=True, blank=True)

    class Meta:
        ordering = ['content_order']





    def save(self, *args, **kwargs):
        desired_order = self.content_order
        CourseContents.objects.filter(content_order__gte=desired_order).update(content_order=models.F('content_order') + 1)
        super(CourseContents, self).save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.course}: Content {self.content_order}"