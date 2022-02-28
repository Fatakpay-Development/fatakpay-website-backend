from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
import csv
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
import datetime
# Register your models here.





@admin.register(Corporate)
class CorporateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("full_name","work_email","company_name", "business_loc", "employee_no", "where_hear", "contact", "created_at","updated_at","is_deleted")
    list_filter  = ['full_name','work_email', ('created_at', DateRangeFilter),]
    
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'save from dates you would like'

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


@admin.register(CountryDialCode)
class CountryDialCodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display        = ("name","dial_code","code")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False