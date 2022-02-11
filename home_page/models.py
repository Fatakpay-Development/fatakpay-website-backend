from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SingUp(models.Model):
    full_name       = models.CharField(max_length=100, blank=True, null=True,)
    email           = models.EmailField(max_length=100, blank=True, null=True,)
    contact         = models.CharField(max_length=10, blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)
    # created_by  = models.ForeignKey('User', on_delete=models.CASCADE, related_name='', blank=True, null=True,)

    def __str__(self): 
        return str(self.full_name)
        
    class Meta:
        db_table = "SingUp"
        verbose_name_plural = 'SingUp'



class WatchVideo(models.Model):
    video           = models.CharField(max_length=100, blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='WatchVideo_User', blank=True, null=True,)
        
    class Meta:
        db_table = "WatchVideo"
        verbose_name_plural = 'WatchVideo'


class Testmonials(models.Model):
    profile_image   =  models.FileField(upload_to = "images/testmonial_profile", blank=True, null=True)
    full_name       = models.CharField(max_length=100, blank=True, null=True,)
    designation     = models.CharField(max_length=100, blank=True, null=True,)
    logo            =  models.FileField(upload_to = "images/testmonial_logo", blank=True, null=True)
    rating          = models.IntegerField(blank=True, null=True,)
    title           = models.CharField(max_length=10, blank=True, null=True,)
    description     = models.TextField(max_length=10, blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Testmonials_User', blank=True, null=True,)

    def __str__(self): 
        return str(self.full_name)
        
    class Meta:
        db_table = "Testmonials"
        verbose_name_plural = 'Testmonials'