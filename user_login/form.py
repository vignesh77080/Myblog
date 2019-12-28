from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user_login.models import ProfileUser, Post

class UserLogin(forms.ModelForm):

    class Meta():
        model = User
        fields = ['username', 'password']

class RegistrationForm(UserCreationForm):

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):

    class Meta():
        model = ProfileUser
        fields = ['profilepics']

class ProfileUpdate(forms.ModelForm):

    class Meta():
        model = User
        fields = ['username', 'email']

class PostCreation(forms.ModelForm):

    class Meta():
        model = Post
        fields = '__all__'
        exclude = ['created_by', 'last_modified']