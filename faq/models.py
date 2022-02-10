from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faq(models.Model):
    question       =    models.CharField(max_length=100, null=True, blank=True)
    answer         =    models.CharField(max_length=100, null=True, blank=True)
    created_at      =   models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    updated_at      =   models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_deleted      =   models.BooleanField(default=False)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'Faq'

    #verbose

    verbose_name_plural = 'Faq'