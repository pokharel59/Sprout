from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Subject(models.Model):
     subject_id = models.AutoField(primary_key=True, null=False)
     subject_name = models.CharField(max_length=100, null=False)
     subject_image = CloudinaryField('image', null=False)
     subject_desc = models.CharField(max_length=255, null=False)
     created_at = models.DateTimeField(auto_now_add=True)
 
     def __str__(self):
          return self.subject_name

class Content(models.Model):
     content_id = models.AutoField(primary_key=True, null=False)
     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
     content_title = models.CharField(max_length=50, null=False)
     content_desc = models.CharField(max_length=100, null=False)
     content_icon = CloudinaryField('image', null=False)
     created_at = models.DateTimeField(auto_now_add=True)

     
     def __str__(self):
          return self.content_title

class Activity(models.Model):
     activity_id = models.AutoField(primary_key=True, null=False)
     content = models.ForeignKey(Content, on_delete=models.CASCADE, null=False)
     activity_title = models.CharField(max_length=100, null=False)
     activity_icon = CloudinaryField('image', null=False)
     scene_file_name = models.CharField(max_length=100, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

     
     def __str__(self):
          return self.activity_title
