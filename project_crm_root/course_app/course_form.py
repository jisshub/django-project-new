from .models import CouseModel
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = CouseModel
        fields = '__all__'
