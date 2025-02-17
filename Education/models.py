from django.db import models

# Create your models here.
class Education(models.Model):
    education_title = models.CharField(max_length=200, null=True,blank=True)  # Education का टाइटल (e.g., "Bachelor of Arts")
    education_h1 = models.CharField(max_length=255, null=True,blank=True)
    education_name = models.CharField(max_length=255, null=True,blank=True)  
    institution_name = models.CharField(max_length=255, null=True,blank=True)  
    

class Skills(models.Model):
    skill_name = models.CharField(max_length=255, null=True,blank=True) 
    skill_image = models.ImageField(upload_to='Portfolio_image/', blank=True, null=True) 