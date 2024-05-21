from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	birth_date = models.DateField(blank=True, null=True)


class UserProfile(models.Model):
	bio = models.CharField(max_length=150, null=True, blank=True)
	phone_number = models.CharField(max_length=10, null=True, blank=True)
	#birth_date = models.DateField(blank=True, null=True)
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
