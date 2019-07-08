from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Venue(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=10)
    phone=models.CharField(max_length=15,blank=True)
    web=models.URLField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,blank=True)

    def __str__(self):
    	return self.name

class Event(models.Model):
	name=models.CharField(max_length=50)
	venue=models.ForeignKey(Venue,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	manager=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
	description=models.TextField(blank=True)

	def __str__(self):
		return self.name