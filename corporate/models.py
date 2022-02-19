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
    contact         = models.CharField(max_length=15, blank=True, null=True,)
  
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)

    def __str__(self): 
        return str(self.full_name)
    
    class Meta:
        db_table = "Corporate"
        verbose_name_plural = 'Corporate'