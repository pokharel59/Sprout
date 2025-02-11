from django.db import models

# # Create your models here.
# class Students(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(unique=True)

#     def __str__(self):
#          return f"{self.first_name} {self.last_name}"

class User(models.Model):
     ACTIVE = "Active"
     INACTIVE = "Inactive"
     USER_STATUS_CHOICES = [
          (ACTIVE, "Active"),
          (INACTIVE, "Inactive")
     ]

     user_id = models.AutoField(primary_key=True, null=False)
     user_name = models.CharField(max_length=100, null=False)
     user_email = models.CharField(max_length=100, null=False)
     user_status = models.CharField(
          max_length=50,
          choices=USER_STATUS_CHOICES,
          default=ACTIVE, 
          null=False
          )
     joined_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.user_name

class Subject(models.Model):
     subject_id = models.AutoField(primary_key=True, null=False)
     subject_name = models.CharField(max_length=100, null=False)
     subject_image = models.CharField(max_length=100, blank=True, null=True)
     subject_desc = models.CharField(max_length=255, null=False)
     created_at = models.DateTimeField(auto_now_add=True)
 
     def __str__(self):
          return self.subject_name

class Content(models.Model):
     content_id = models.AutoField(primary_key=True, null=False)
     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
     content_title = models.CharField(max_length=50, null=False)
     content_desc = models.CharField(max_length=100, null=False)
     content_icon = models.CharField(max_length=100, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

     
     def __str__(self):
          return self.content_title

class Activity(models.Model):
     activity_id = models.AutoField(primary_key=True, null=False)
     content = models.ForeignKey(Content, on_delete=models.CASCADE, null=False)
     activity_title = models.CharField(max_length=100, null=False)
     activity_icon = models.CharField(max_length=100, blank=True, null=True)
     scene_file_name = models.CharField(max_length=100, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

     
     def __str__(self):
          return self.activity_title
