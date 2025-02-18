from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
     ACTIVE = "Active"
     INACTIVE = "Inactive"
     USER_STATUS_CHOICES = [
          (ACTIVE, "Active"),
          (INACTIVE, "Inactive"),
     ]

     user_status = models.CharField(
          max_length=50,
          choices=USER_STATUS_CHOICES,
          default=ACTIVE,
          null=False
     )
