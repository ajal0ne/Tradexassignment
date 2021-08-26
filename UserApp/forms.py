from django import forms
from . models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'created_at':DateInput(),'updated_at':DateInput()}
        fields = ['user','text','created_at','updated_at']
