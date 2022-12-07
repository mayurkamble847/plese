from django.db import models

# # Create your models here.
# class Contact(models.Model):
#     name=models.CharField(max_length=20)
#     email=models.CharField(max_length=20)
#     phone=models.CharField(max_length=12)
#     desc=models.TextField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=122,blank=True,null=True)
    email=models.CharField(max_length=122,blank=True,null=True)
    phone=models.CharField(max_length=122,blank=True,null=True)
    desc=models.CharField(max_length=122,blank=True,null=True)
