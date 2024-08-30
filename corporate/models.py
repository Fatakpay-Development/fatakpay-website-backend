from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Corporate(models.Model):

    
    WHERE_HEAR_CHOICES = [
                        ("Referral", 'Referral'),
                        ("Search_Engine", 'Search_Engine'),
                        ("Another_Website", 'Another_Website'),
                        ("Social_Media", 'Social_Media'),
                        ("WhatsApp", 'WhatsApp'),
                        ("Ad", 'Ad'),
                        ("SMS", 'SMS'),
                        ("Other", 'Other'),
                        ]

    
    full_name       =   models.CharField(max_length=100, null=True, blank=True)
    work_email      =   models.CharField(max_length=100, null=True, blank=True)
    company_name    =   models.CharField(max_length=100, null=True, blank=True)
    business_loc    =   models.CharField(max_length=100, null=True, blank=True)
    employee_no     =   models.IntegerField(null=True, blank=True)
    where_hear      =   models.CharField(max_length=100, choices=WHERE_HEAR_CHOICES, default="Other")
    country_code    =   models.CharField(max_length=10, blank=True, null=True,)
    contact         =   models.CharField(max_length=15, blank=True, null=True,)
  
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)

    def __str__(self): 
        return str(self.full_name)
    
    class Meta:
        db_table = "Corporate"
        verbose_name_plural = 'Corporate'


class CountryDialCode(models.Model):
    name        =   models.CharField(max_length=100, null=True, blank=True)
    dial_code   =   models.CharField(max_length=100, null=True, blank=True)
    code        =   models.CharField(max_length=100, null=True, blank=True)

    def __str__(self): 
        return str(self.name)
    
    class Meta:
        db_table = "CountryDialCode"
        verbose_name_plural = 'CountryDialCode'


class ScheduleDemo(models.Model):
    full_name = models.CharField(max_length=100, null= True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    conatct = models.CharField(max_length=100, null=True, blank=True)
    pricing = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=True)

    def __str__(self):
        return str(self.full_name)
    
    class Meta:
        db_table = "ScheduleDemo"
        verbose_name_plural = 'ScheduleDemo' 





