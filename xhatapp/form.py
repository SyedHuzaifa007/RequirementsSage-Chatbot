from django import forms
from django.contrib.auth.models import User
from xhatapp.models import SaveQueries
from .models import UserInfo
class usserform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo  # Assuming UserInfo is your user profile model
        fields = ['password']  # Include other fields as needed

    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

from django import forms
from .models import UserInfo

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user', 'username']
        from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)