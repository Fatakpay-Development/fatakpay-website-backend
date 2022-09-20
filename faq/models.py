from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class FaqCategory(models.Model):

    category        =   models.CharField(max_length=255, blank=True, null=True)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)

    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self): 
        return str(self.category)
   
    class Meta:
        db_table = 'faq_category'
        verbose_name_plural = 'Faq Category'




class Faq(models.Model):
    USER_CHOICES = [
                    ('U', 'user'),
                    ('E', 'employee'),
                    ('A', 'app'),
                    ('Fatakpay Card', 'Fatakpay Card'),
                    ('Payments', 'Payments'),
                    ('Get Started', 'Get Started')
                ]
    user_type   =   models.CharField(max_length=255, choices=USER_CHOICES, default="user")
    category    =   models.ForeignKey(FaqCategory, on_delete=models.CASCADE, blank=True, null=True)

    question        =   models.TextField(null=True, blank=True)
    answer          =   models.TextField(null=True, blank=True)
    priority        =   models.FloatField(null=True, blank=True)
    is_important    =   models.BooleanField(default=False)
    
    
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self): 
        return str(self.question)
   
    class Meta:
        db_table = 'Faq'
        verbose_name_plural = 'Faq'


class Resources(models.Model):
    video           = models.FileField(blank=True, null=True,)

    created_at      = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    priority        =  models.FloatField(null=True, blank=True)
    is_deleted      = models.BooleanField(default = False)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
        
    def __str__(self): 
        return str(self.video)

    class Meta:
        db_table = "Resources"
        verbose_name_plural = 'Resources'
