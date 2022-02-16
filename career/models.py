from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Career(models.Model):
    image               = models.FileField(upload_to = "images/watch_video", blank=True, null=True)
    designation         = models.CharField(max_length=100, blank=True, null=True,)
    location            = models.CharField(max_length=100, blank=True, null=True,)
    report_to           = models.CharField(max_length=100, blank=True, null=True,)
    employee_type       = models.CharField(max_length=250, blank=True, null=True,)
    expect_from_you     = models.TextField(max_length=250, blank=True, null=True,)
    ideal_candidate     = models.TextField(max_length=250, blank=True, null=True,)
    love_working_fpay   = models.TextField(max_length=250, blank=True, null=True,)
    perks_benefits      = models.TextField(max_length=250, blank=True, null=True,)

    created_at          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at          = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted          = models.BooleanField(default = False)
    created_by          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Career_User', blank=True, null=True,)

    def __str__(self):
        return str(self.designation)
    
    class Meta:
        db_table = "Career"
        verbose_name_plural = 'Career'


class ApplicationForm(models.Model):
    full_name       = models.CharField(max_length=100, blank=True, null=True,)
    email           = models.CharField(max_length=100, blank=True, null=True,)
    contact         = models.CharField(max_length=15, blank=True, null=True,)
    linkedin_link   = models.TextField(blank=True, null=True)
    resume          = models.FileField(upload_to = "images/resume", blank=True, null=True)
    designation     = models.ForeignKey('Career', on_delete=models.CASCADE, related_name='ApplicationForm_Career', blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      = models.BooleanField(default = False)

    def __str__(self): 
        return str(self.full_name)
        
    class Meta:
        db_table = "ApplicationForm"
        verbose_name_plural = 'ApplicationForm'