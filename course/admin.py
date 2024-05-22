from django.contrib import admin

from .models import Course,CourseContents,FileField

# Inline for CourseContents within CourseAdmin
class CourseContentsInline(admin.TabularInline):
    model = CourseContents
    extra = 1


# Custom admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentsInline]
    list_display = ('title', 'description', 'course_price', 'content_price')


admin.site.register(FileField)



admin.site.register(Course, CourseAdmin)
