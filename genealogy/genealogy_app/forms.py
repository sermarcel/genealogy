from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    login = forms.CharField(
        initial = "",
        label='Login',
        max_length=32,
        
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        initial = "",  # wartosc poczatkowa        
        label='Password',
        required=False,
        widget=forms.PasswordInput(),        
    )

class CreateAccountForm(forms.Form):
    login = forms.CharField(
        label='Username',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,

    )
    email = forms.CharField(
        label='Email',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )