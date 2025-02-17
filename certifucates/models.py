from django.db import models

# Create your models here.

class Certificate(models.Model):

    certificate_name = models.CharField(max_length=255,blank=True, null=True)  
    certificate_url = models.URLField(blank=True, null=True) 


