from django.db import models

# Create your models here.
class User(models.Model):
     ACTIVE = "Active"
     INACTIVE = "Inactive"
     USER_STATUS_CHOICES = [
          (ACTIVE, "Active"),
          (INACTIVE, "Inactive")
     ]

     user_id = models.AutoField(primary_key=True, null=False)
     user_name = models.CharField(max_length=100, null=False)
     user_email = models.CharField(max_length=100, unique=True, null=False)
     user_status = models.CharField(
          max_length=50,
          choices=USER_STATUS_CHOICES,
          default=ACTIVE, 
          null=False
          )
     joined_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.user_name
