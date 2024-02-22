from django.forms import EmailField, ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
