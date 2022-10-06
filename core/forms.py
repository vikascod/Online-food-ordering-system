from django import forms
from core.models import Food, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'



class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        