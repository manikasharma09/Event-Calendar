from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
	event_name=models.CharField(max_length=50)
	venue=models.CharField(max_length=50)
	date=models.DateTimeField(default=timezone.now)
	email=models.EmailField(max_length=100,blank=True)
	description=models.TextField(blank=True)

	def __str__(self):
		return self.event_name
