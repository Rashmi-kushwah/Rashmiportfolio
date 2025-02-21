from django.db import models

# Create your models here.
class Projects(models.Model):
   
    project_name1 = models.CharField(max_length=255, null=True,blank=True) 
    project_description1 = models.TextField(blank=True, null=True)
    project_image1 = models.ImageField(upload_to='Portfolio_images/', blank=True, null=True) 
    github_link = models.URLField(max_length=500, blank=True, null=True)
    live_link = models.URLField(max_length=500, blank=True, null=True)
