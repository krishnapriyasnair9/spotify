from django import forms

from django.contrib.auth.forms import UserCreationForm
from user.models import User,Songs,Artists


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["first_name",
                  "username",
                  "email",
                  "password1",
                  "password2",
                  "phone",
                  ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),


        }
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
class SongsForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields="__all__"
        widgets={
            #"cover_pic":forms.ImageField(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dateofrelease":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }
class ArtistsForm(forms.ModelForm):
    class Meta:
        model=Artists
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "DOB":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "bio":forms.Textarea(attrs={"class":"form-control"})
        }
