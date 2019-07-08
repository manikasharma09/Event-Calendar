from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
import time
from .models import *

@shared_task
def send_notification():
	print('here i am')