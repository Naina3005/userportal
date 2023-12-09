# file_upload_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import UploadedFile

class UserRegistrationForm(UserCreationForm):
    # Add any additional fields if needed
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
class FileShareForm(forms.Form):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text='Select users to share the file with' 
    )