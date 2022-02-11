from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AboutUs(models.Model):
    CHOICE_TEAM = 'T'
    CHOICE_EMP = 'E'
    
    EMPLOYEE_CHOICES = [
                        (CHOICE_TEAM, 'team'),
                        (CHOICE_EMP, 'employee')]

    
    employee_name   =   models.CharField(max_length=100, null=True, blank=True)
    designation     =   models.CharField(max_length=100, null=True, blank=True)
    profile         =   models.ImageField(upload_to="images/aboutus_profile", blank=True, null=True)
    description     =   models.TextField(blank=True, null=True)
    employee_type   =   models.CharField(max_length=4, choices=EMPLOYEE_CHOICES, default=CHOICE_TEAM)
    linkedin_link   =   models.URLField(max_length =100, blank=True, null=True)
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = "AboutUs"
        verbose_name_plural = 'AboutUs'