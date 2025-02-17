from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render

from  project.models import Projects
from  Aboutus.models import Aboutus
from  Education.models import Education
from  Education.models import Skills
from  certifucates.models import Certificate
from  Contactform.models import Contact




def Header(request):
    return render (request,'Header.html')

def Footer(request):
    return render (request,'Footer.html')

def Certificatedt(request):

    certificate_data = Certificate.objects.all()
    print("certificates",certificate_data)
 
    return render(request, 'Certificate.html', {'certificate_data': certificate_data})
from django.shortcuts import render, redirect

from django.contrib import messages

def Home(request):
  
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Received Data: Name={name}, Email={email}, Message={message}")  # Debugging

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/')
        else:
            messages.error(request, "All fields are required!")
    about_data = Aboutus.objects.all()
    certificate_data = Certificate.objects.all()
    Projects_data = Projects.objects.all()
    Education_data = Education.objects.all()
    Skills_data = Skills.objects.all()
    contact_data = Contact.objects.all()

    return render(request, 'Home.html', {
        'certificate_data': certificate_data,
        'Skills_data': Skills_data,
        'Education_data': Education_data,
        'Projects_data': Projects_data,
        'about_data': about_data,
        # 'contact_data': contact_data,
    })

def Skilldt(request):
    Skills_data = Skills.objects.all()
    print('Skills_dataaaaa',Skills_data) 
    return render (request,'Skills.html',{'Skills_data': Skills_data})

def Educationdt(request):
    Education_data = Education.objects.all()
    print('Educationxxxxxxxxxxxxxxxxxxxxxxxxxxx_data',Education_data) 
    return render (request,'Skills.html',{'Education_data': Education_data})



def About(request):
    about_data = Aboutus.objects.all()
    print('about_dataaaa',about_data)  # Debugging के लिए
    return render(request, 'About.html', {'about_data': about_data})


def Project(request):
    Projects_data = Projects.objects.all()
    print("ddfc",Projects_data)

    return render(request, 'Projects.html', {'Projects_data': Projects_data})

from django.shortcuts import render, redirect



from django.shortcuts import render, redirect
from django.contrib import messages

def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Received Data: Name={name}, Email={email}, Message={message}")  # Debugging

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Ensure 'contact' URL is correct
        else:
            messages.error(request, "All fields are required!")

    # GET request ke case me render karna h
    return render(request, "contact.html")
