"""
URL configuration for Rashmi_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

from django.urls import path , include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Portfolio_Home, name='home'),
    path('header/', views.Portfolio_Header, name='header'),
    path('footer/', views.Portfolio_Footer, name='footer'),
    path('certificate/', views.Portfolio_Certificatedt, name='certificate'),
    path('projects/', views.Portfolio_Project, name='projects'),
    path('skills/', views.Portfolio_Skilldt, name='skills'),
    path('Educationdt/', views.Portfolio_Educationdt, name='education'),
    path('contact/', views.Portfolio_contact_form, name='contact'),
    path('about/', views.Portfolio_About, name='about'),

  
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)