from .models import Course,CourseContents,FileField,VideoLinks


from django import forms
# = FileField.objects.all()
class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContents
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['files'].queryset.order_by('coursecontents')
            self.fields['video_link'].queryset = self.instance.video_link.all()
        else:
            self.fields['files'].queryset = FileField.objects.none()
            self.fields['video_link'].queryset = VideoLinks.objects.none()


class CourseForm(forms.ModelForm):
    total_content = forms.IntegerField(label='Total Content', required=False,widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Course
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['total_content'].initial = CourseContents.objects.filter(course = self.instance).count()
