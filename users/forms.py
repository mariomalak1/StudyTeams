from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, required=True)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, required=True)