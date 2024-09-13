from django import forms
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Course,CourseContents,FileField,VideoLinks,GoogleDriveLinks,RegisterCourse
from .forms import *
from django.contrib.admin.actions import delete_selected as delete_selected_

from .models import Course, CourseContents, FileField, VideoLinks


class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContents
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['files'].queryset = FileField.objects.all()
        self.fields['video_link'].queryset = VideoLinks.objects.all()


# Inline for CourseContents within CourseAdmin
class CourseContentsInline(admin.TabularInline):
    model = CourseContents
    form = CourseContentForm
    extra = 1



class ModelAdmin2(admin.ModelAdmin):

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet) -> None:
        for i in queryset:
            if i.delete_status == True:
                super().delete_queryset(request, queryset)
            else:   
                i.delete_status = True
                i.save()

        


# Custom admin class for the Course model
class CourseAdmin(ModelAdmin2):
    inlines = [CourseContentsInline]
    list_display = ('title', 'description', 'course_price', 'content_price','total_content')
    form = CourseForm
    def total_content(self,obj):
        return CourseContents.objects.filter(course = obj).count()





admin.site.register(FileField)

admin.site.register(VideoLinks)

admin.site.register(Course, CourseAdmin)

admin.site.register(GoogleDriveLinks)
admin.site.register(RegisterCourse)