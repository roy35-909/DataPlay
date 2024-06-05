from django.contrib import admin

from .models import Course,CourseContents,FileField,VideoLinks


from django import forms

class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContents
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['files'].queryset = self.instance.files.all()
            self.fields['video_link'].queryset = self.instance.files.all()
        else:
            self.fields['files'].queryset = FileField.objects.none()
            self.fields['video_link'].queryset = FileField.objects.none()


# Inline for CourseContents within CourseAdmin
class CourseContentsInline(admin.TabularInline):
    model = CourseContents
    form = CourseContentForm
    extra = 1


# Custom admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentsInline]
    list_display = ('title', 'description', 'course_price', 'content_price')





admin.site.register(FileField)

admin.site.register(VideoLinks)

admin.site.register(Course, CourseAdmin)

