# user_login/forms.py

from django import forms
import re

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError('Username must contain only letters, numbers, and underscores.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', password):
            raise forms.ValidationError('Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.')
        return password
#heyy