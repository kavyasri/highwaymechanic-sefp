from django.db import models
from hm import codes
from django.contrib.auth.models import User as auth_user

class Status(models.Model):
	code 		= models.IntegerField(default=0,editable=True) 
	code_message 	= models.TextField(default='NA')
	 

class UserProfile(models.Model):
	user 		= models.OneToOneField(auth_user)
	is_mechanic	= models.BooleanField(default=False)	
	longitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	latitude 	= models.DecimalField(max_digits=9, decimal_places=6)
	mobile		= models.CharField(max_length=12,null=True)
	
	def __str__(self):
		return str(self.user)

	def set_longitude(self, longitude):
		self.longitude = longitude

	def set_latitude(self, latitude):
		self.latitude = latitude

	def get_longitude(self):
		return self.longitude

	def get_latitude(self):
		return self.latitude

class Service(models.Model):
	name 		= models.CharField(max_length=150)
	description 	= models.TextField()
	def __str__(self):
		return self.name

class Chat(models.Model):
	sender 		= models.ForeignKey(auth_user, related_name='sender')
	receiver 	= models.ForeignKey(auth_user, related_name='receiver')
	message 	= models.TextField()
	timestamp 	= models.DateTimeField()
	read 		= models.BooleanField(default=False)

	

		

