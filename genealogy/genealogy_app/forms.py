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

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
