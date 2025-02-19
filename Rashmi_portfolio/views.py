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



def Portfolio_Home(request):
  

    return render(request, 'index.html')
        