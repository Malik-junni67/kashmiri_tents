# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Tent
from django.contrib.auth.forms import UserCreationForm

class TentForm(forms.ModelForm):
    class Meta:
        model = Tent
        fields = ['name', 'photo', 'rate', 'rating']



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Set username as email
        if commit:
            user.save()
        return user



