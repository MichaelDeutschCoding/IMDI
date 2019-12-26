from django.forms import Form, CharField, EmailField, TextInput, PasswordInput, EmailInput
from django.contrib.auth.models import User

class SignupForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control',
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control',
    }))

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            msg = f"Sorry, the username '{username}' is already taken."
            self.add_error('username', msg)

class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-25',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-25',
    }))
