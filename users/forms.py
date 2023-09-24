from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userProfile
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(max_length=150,label="Last Name")
    first_name = forms.CharField(max_length=150,label="First Name")
    
    class Meta:
        model=User
        fields =['username','email','last_name','first_name','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField
    class Meta:
        model=User
        fields =['username','email']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['image']
        
    