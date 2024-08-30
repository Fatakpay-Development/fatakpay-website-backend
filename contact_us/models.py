from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactUs(models.Model):
    full_name       =   models.CharField(max_length=100, null=True, blank=True)
    email           =   models.CharField(max_length=100, null=True, blank=True)
    message         =   models.TextField(null=True, blank=True)
    
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)

    def __str__(self): 
        return str(self.full_name)
    
    class Meta:
        db_table = "ContactUs"
        verbose_name_plural = 'ContactUs'

class ffplContactUser(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_name)
    
    class Meta:
        db_table = "ffplContactUser"
        verbose_name_plural = 'ffplContactUser'