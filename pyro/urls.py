from django.contrib import admin
from django.urls import path
from Mainapp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.homepage),
    path('about/', mainapp.aboutpage),
    path('service/',mainapp.servicepage),
    path('project/',mainapp.projectpage),
    path('blog/', mainapp.blogpage),
    path('team/',mainapp.teampage),
    path('testimonial/',mainapp.testimonialpage),
    path('contact/',mainapp.contactpage),
]
