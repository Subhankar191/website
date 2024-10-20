# login_project/registration/forms.py
from django import forms
from .models import User  # Import the User model from your models.py file

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','phone', 'password']
