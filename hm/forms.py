from django import forms
from hm.models import Service
from django.contrib.auth.forms import AuthenticationForm
from hm import templatenames, methods
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
	username	= forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control','label':'Email'}) )	
	password	= forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}) )

class RegisterForm(forms.Form):
	username  	= forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'id':'username'}) )	
	password	= forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password'}) )
	password_again  = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password_again'}) )
	iamamechanic	= forms.BooleanField(widget=forms.CheckboxInput(), required=False )
	def clean_username(self):
        	try:
            		user = User.objects.get(username__iexact=self.cleaned_data['username'])
        	except User.DoesNotExist:
            		return self.cleaned_data['username']
        	raise forms.ValidationError(("This email has been taken. Please try another one."))
 
    	def clean(self):
        	if 'password' in self.cleaned_data and 'password_again' in self.cleaned_data:
            		if self.cleaned_data['password'] != self.cleaned_data['password_again']:
                		raise forms.ValidationError(("Passwords did not match. Please enter same password as first."))
        	return self.cleaned_data	

class SelectServiceForm(forms.Form):
	service		= forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control', 'rows':'50', 'cols':'100'}), 							choices=Service.objects.values_list('id','name'))	

