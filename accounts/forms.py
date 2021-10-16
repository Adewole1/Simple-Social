from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=65, help_text='Enter a valid email address')
    
    class meta:
        model = get_user_model()
        fields = ("first_name","last_name","username", "email", "password1", "password2")
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email address'

