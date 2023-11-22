from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SignUp(models.Model):
    full_name       = models.CharField(max_length=100, blank=True, null=True,)
    email           = models.CharField(max_length=100, blank=True, null=True,)
    country_code    = models.CharField(max_length=10, blank=True, null=True,)
    contact         = models.CharField(max_length=15, blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)

    def __str__(self): 
        return str(self.full_name)
        
    class Meta:
        db_table = "SignUp"
        verbose_name_plural = 'SignUp'



class WatchVideo(models.Model):
    video           = models.FileField(blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='WatchVideo_User', blank=True, null=True,)
        
    def __str__(self): 
        return str(self.video)

    class Meta:
        db_table = "WatchVideo"
        verbose_name_plural = 'WatchVideo'


class Testmonials(models.Model):
    profile_image   = models.FileField(upload_to = "images/testmonial_profile", blank=True, null=True)
    full_name       = models.CharField(max_length=100, blank=True, null=True,)
    designation     = models.CharField(max_length=100, blank=True, null=True,)
    logo            = models.FileField(upload_to = "images/testmonial_logo", blank=True, null=True)
    rating          = models.IntegerField(blank=True, null=True,)
    title           = models.CharField(max_length=255, blank=True, null=True,)
    description     = models.TextField(blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Testmonials_User', blank=True, null=True,)

    def __str__(self): 
        return str(self.full_name)
        
    class Meta:
        db_table = "Testmonials"
        verbose_name_plural = 'Testmonials'

class ReferCompany(models.Model):
    manager_name = models.CharField(max_length=100, blank=False, null=False)
    manager_email = models.CharField(max_length=100, blank=False, null=False)
    company_name = models.CharField(max_length=100, blank=False, null=False)
    number_of_employees = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.manager_name)
    
    class meta:
        db_table = "ReferCompany"
        verbose_name_plural = "ReferCompany"