from django.db import models

from django.db import models

class PortfolioImage(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  # Position field
    description = models.TextField()  # Description field
    image = models.ImageField(upload_to='portfolio_images/')  # Image field

    def __str__(self):
        return self.name



# Create your models here.
class Aboutus(models.Model):
    About_title = models.CharField(max_length=100)  # About का title
    About_p = models.TextField()  # About section का content
    About_Linkedin = models.CharField(max_length=255, blank=True, null=True)  # LinkedIn link
    About_email = models.EmailField(max_length=255, blank=True, null=True)  # Email field
    About_City = models.CharField(max_length=100, blank=True, null=True)  # City name
    About_Country = models.CharField(max_length=100, blank=True, null=True)  # Country name
    profile_image = models.ImageField(upload_to='Portfolio_images/', blank=True, null=True) 