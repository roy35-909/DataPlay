from django.contrib import admin

from .models import Course,CourseContents,FileField,VideoLinks
from .forms import *




# Inline for CourseContents within CourseAdmin
class CourseContentsInline(admin.TabularInline):
    model = CourseContents
    form = CourseContentForm
    extra = 1


# Custom admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentsInline]
    list_display = ('title', 'description', 'course_price', 'content_price','total_content')
    form = CourseForm
    def total_content(self,obj):
        return CourseContents.objects.filter(course = obj).count()





admin.site.register(FileField)

admin.site.register(VideoLinks)

admin.site.register(Course, CourseAdmin)

