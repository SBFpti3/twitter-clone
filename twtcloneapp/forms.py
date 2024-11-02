from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm) :

    class Meta :

        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        for field in self.fields.values() :
            field.widget.attrs.update({
                'class' : 'input-field',
                'placeholder' : field.label,
            })

class LoginForm(AuthenticationForm) :
    
    username = forms.CharField(widget=TextInput(), label="Username")
    password = forms.CharField(widget=PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values() :
            field.widget.attrs.update({
                'class' : 'input-field',
                'placeholder' : field.label,
            })