from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Dog(models.Model):
	
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	
	def __str__(self):
		return self.first_name    		

	def get_absolute_url(self):
		return u'/dashboard/dog/'

class Venu(models.Model):
	google_place_id = models.CharField(max_length=200)
	venu_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=50)
	trading_hours = models.TextField()
	desc = models.TextField()
	
	def __str__(self):
		return self.venu_name    		

	def get_absolute_url(self):
		return u'/dashboard/'

class Customer(models.Model):
	# google_place_id = models.CharField(max_length=200)
	customer_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=50)
	desc = models.TextField()
	create_date = models.DateField(default=date.today)
	
	def __str__(self):
		return self.customer_name    		

	def get_absolute_url(self):
		return u'/dashboard/customer/'
