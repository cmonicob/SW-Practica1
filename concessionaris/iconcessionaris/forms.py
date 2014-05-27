from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm	
from models import *

class ClientForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)   

    class Meta:
        model = User
        exclude = ('date', 'last_login', 'groups','is_superuser','user_permissions','is_staff','is_active','date_joined',)

    def save(self, commit=True):
        user = super(ClientForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
	
class OrderForm(ModelForm):	
	class Meta:	
		model = Compra

class CarDealerForm(ModelForm):	
	class Meta:	
		model = Concessionari

class BrandForm(ModelForm):	
	class Meta:	
		model = Marca	

class ReviewForm(ModelForm):	
	class Meta:	
		model = Review	
	

