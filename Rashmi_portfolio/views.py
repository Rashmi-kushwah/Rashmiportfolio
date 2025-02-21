from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from  project.models import Projects
from  Aboutus.models import Aboutus
from  Aboutus.models import PortfolioImage
from  Education.models import Education
from  Education.models import Skills
from  certifucates.models import Certificate
from  Contactform.models import Contact
from django.shortcuts import render, redirect
from django.contrib import messages



def Portfolio_Header(request):
    return render (request,'Header.html')

def Portfolio_Footer(request):
    return render (request,'Footer.html')


def Portfolio_Home(request):
  
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
    portfolio_images = PortfolioImage.objects.all()
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",portfolio_images)

    return render(request, 'index.html', {
        'certificate_data': certificate_data,
        'Skills_data': Skills_data,
        'Education_data': Education_data,
        'Projects_data': Projects_data,
        'about_data': about_data,
        'portfolio_images': portfolio_images,
        # 'contact_data': contact_data,
    })



# def Portfolio_contact_form(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         print(f"Received Data: Name={name}, Email={email}, Message={message}")  # Debugging

#         if name and email and message:
#             Contact.objects.create(name=name, email=email, message=message)
#             messages.success(request, "Your message has been sent successfully!")
#             return redirect('/')  # Ensure 'contact' URL is correct
#         else:
#             messages.error(request, "All fields are required!")

#     # GET request ke case me render karna h
#     return render(request, "index.html")
def Portfolio_contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Received Data: Name={name}, Email={email}, Message={message}")  # Debugging

        if name and email and message:
            # Check if a contact with this email already exists
            if Contact.objects.filter(email=email).exists():
                messages.info(request, "You have already submitted your details!")
                return redirect('/')  # Redirect without saving duplicate data
            else:
                Contact.objects.create(name=name, email=email, message=message)
                messages.success(request, "Your message has been sent successfully!")
                return redirect('/')
        else:
            messages.error(request, "All fields are required!")
    
    # For GET request, simply render the index page
    return render(request, "index.html")
