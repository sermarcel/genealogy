from django import forms


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