from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faq(models.Model):
    USER_CHOICES = [
                    ('U', 'user'),
                    ('E', 'employee'),
                    ('A', 'app'),

                ]
    user_type   =   models.CharField(max_length=4, choices=USER_CHOICES, default="user")

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

