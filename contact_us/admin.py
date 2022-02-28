from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
import csv
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
import datetime
# Register your models here.


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("full_name", "email", "created_at","updated_at","is_deleted")
    list_filter  = ['full_name','email', ('created_at', DateRangeFilter),]
    
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'save from dates you would like'

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False