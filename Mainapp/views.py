from django.shortcuts import render
from django.contrib import auth,messages

from .models import *

def homepage(Request):
    return render(Request,"index.html")

def aboutpage(Request):
    return render(Request,"about.html")

def servicepage(Request):
    return render(Request,"service.html")

def projectpage(Request):
    return render(Request,"project.html")

def blogpage(Request):
    return render(Request,"blog.html")

def teampage(Request):
    return render(Request,"team.html")


def testimonialpage(Request):
    return render(Request,"testimonial.html")


def contactpage(Request):
    if(Request.method=="POST"):
        c = Contact_form()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.save()
        messages.success(Request,"Thanks to Share Your Query With Us!!! Our Team Will Contact You Soon!!!")

    return render(Request,"contact.html")
