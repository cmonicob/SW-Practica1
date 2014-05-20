from django.forms import ModelForm	
from models import *
  
class ClientForm(ModelForm):	
	class Meta:	
		model = User	
		exclude = ('date', 'last_login', 'groups','is_superuser','user_permissions','is_staff','is_active','date_joined')
	
class OrderForm(ModelForm):	
	class Meta:	
		model = Compra

class CarDealerForm(ModelForm):	
	class Meta:	
		model = Concessionari

class BrandForm(ModelForm):	
	class Meta:	
		model = Marca	
	

