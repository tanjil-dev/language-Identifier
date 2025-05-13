# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()  # This will automatically use CustomUser
        fields = ['username', 'email', 'password1', 'password2']
