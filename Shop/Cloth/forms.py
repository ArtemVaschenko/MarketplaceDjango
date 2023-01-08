from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].emty_label = "not chosen"

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form_input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    email = forms.CharField(label='email', widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'email', 'password2']
