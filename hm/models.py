from django.db import models
from hm import codes
from django.contrib.auth.models import User as auth_user

class Status(models.Model):
	code 		= models.IntegerField(default=0,editable=True) 
	code_message 	= models.TextField(default='NA') 

class Mechanic(models.Model):
	user 		= models.OneToOneField(auth_user)
	longitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	latitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	services 	= models.TextField(default='NA') 
	mobile 		= models.CharField(max_length=12)
	credit 		= models.IntegerField(default=0,editable=True)	

class Driver(models.Model):
	user 		= models.OneToOneField(auth_user)
	longitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	latitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	mobile		= models.CharField(max_length=12)	

class Service(models.Model):
	name 		= models.CharField(max_length=150)
	description 	= models.TextField()

class Chat(models.Model):
	sender 		= models.ForeignKey(auth_user, related_name='sender')
	receiver 	= models.ForeignKey(auth_user, related_name='receiver')
	message 	= models.TextField()
	timestamp 	= models.DateTimeField()
	read 		= models.BooleanField(default=False)

class Payment(models.Model):  
	driver		= models.ForeignKey(Driver)
	mechanic	= models.ForeignKey(Mechanic)
	amount		= models.DecimalField(max_digits=10, decimal_places=2)
	statuscode	= models.ForeignKey(Status)
	

class ServiceLog(models.Model):
	driver 		= models.ForeignKey(Driver)
	mechanic 	= models.ForeignKey(Mechanic)
	service		= models.ForeignKey(Service)
	statuscode 	= models.ForeignKey(Status)
	start 		= models.DateTimeField()
	end 		= models.DateTimeField()
		
