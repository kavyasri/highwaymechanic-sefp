from django import forms
from hm.models import Service
class LoginForm(forms.Form):
	email		= forms.EmailField( widget=forms.EmailInput() )	
	password	= forms.CharField( widget=forms.PasswordInput() )

class RegisterForm(forms.Form):
	email		= forms.EmailField( widget=forms.EmailInput() )	
	password	= forms.CharField( widget=forms.PasswordInput() )
	password_again  = forms.CharField( widget=forms.PasswordInput() )
	
class SelectServiceForm(forms.Form):
	service		= forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(),queryset=Service.objects.all())	

