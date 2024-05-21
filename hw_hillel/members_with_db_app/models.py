from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Message(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.text[:500]