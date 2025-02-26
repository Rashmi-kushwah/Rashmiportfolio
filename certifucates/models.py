# from django.db import models

# # Create your models here.

# class Certificate(models.Model):

#     certificate_name = models.CharField(max_length=255,blank=True, null=True)  
#     certificate_url = models.URLField(blank=True, null=True) 


from django.db import models

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=255, blank=True, null=True)  
    certificate_url = models.URLField(blank=True, null=True)  # Link to view certificate
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)  # Upload certificate image
    issued_date = models.DateField(blank=True, null=True)  # Optional: Date of issue
    organization = models.CharField(max_length=255, blank=True, null=True)  # Issuing organization

    def __str__(self):
        return self.certificate_name if self.certificate_name else "Certificate"
