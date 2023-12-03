from django.db import models

class Contact_form(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return str(self.id) +" "+ str(self.name) +" "+ str(self.message)
    
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    img = models.ImageField()
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self(self.name)+" "+ str(self.img)+" "+str(self.designation)
    