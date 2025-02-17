from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Education
from .models import Skills


admin.site.register(Education)
admin.site.register(Skills)
