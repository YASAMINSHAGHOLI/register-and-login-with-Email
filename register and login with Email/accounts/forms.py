from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField



 

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your email ','class':"form-control form-control-lg"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your email ','class':"form-control form-control-lg"}))

    class Meta:
        model = User
        fields = ('email','fullname')
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder':'Enter your email ','class':"form-control form-control-lg"}),
            'fullname' : forms.TextInput(attrs={'placeholder':'Enter your email ','class':"form-control form-control-lg"}),
            'password1' : forms.TextInput(attrs={'placeholder':'Enter your password','class':"form-control form-control-lg"}),
            'password2' : forms.TextInput(attrs={'placeholder':'repeated password','class':"form-control form-control-lg"}),
       }
 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    email =forms.CharField(label='email',widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg' , 'id': 'id_password'}))


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','fullname')
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder':'Enter your account email  here...','class':"form-control form-control-lg"}),
            'fullname' : forms.TextInput(attrs={'placeholder':'Enter your account name here...','class':"form-control form-control-lg"}),
       }


