from django.contrib import admin
from home_page.models import *
from import_export.admin import ImportExportModelAdmin
import csv
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
import datetime
from django.apps import apps

models = apps.get_models()
# Register your models here.

# @admin.register(SignUp)
# class SignUpAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ("full_name", "email","contact","created_at","updated_at","is_deleted")
#     list_filter  = ['full_name','email', ('created_at', DateRangeFilter),]
#     actions      = ["export_as_csv"]
    
#     def get_rangefilter_created_at_default(self, request):
#         return (datetime.date.today, datetime.date.today)

#     def get_rangefilter_created_at_title(self, request, field_path):
#         return 'save from dates you would like'

#     def has_delete_permission(self, request, obj=None):
#         # Disable delete
#         return False

# @admin.register(WatchVideo)
# class WatchVideoAdmin(admin.ModelAdmin):
#     list_display        = ("video", "created_at","updated_at","is_deleted","created_by")
#     readonly_fields     = ('created_by',)

#     def has_delete_permission(self, request, obj=None):
#         # Disable delete
#         return False


#     def save_model(self, request, obj, form, change):
#         platform_user   = User.objects.get(username=request.user)

#         obj.created_by  = platform_user
#         obj.save()


# @admin.register(Testmonials)
# class TestmonialsAdmin(admin.ModelAdmin):
#     list_display        = ("full_name","designation","rating", "title", "description", "created_at","updated_at","is_deleted","created_by")
#     readonly_fields     = ('created_by',)


#     def has_delete_permission(self, request, obj=None):
#         # Disable delete
#         return False

#     def save_model(self, request, obj, form, change):
#         platform_user   = User.objects.get(username=request.user)

#         obj.created_by  = platform_user
#         obj.save()

# @admin.register(ReferCompany)
# class ReferCompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('id', 'manager_name', 'manager_email', 'company_name', 'number_of_employees', 'is_deleted', 'created_at')
#     list_filter = ['manager_name', 'manager_email', 'company_name', ('created_at', DateRangeFilter)]
#     actions      = ["export_as_csv"]

#     def get_rangefilter_created_at_default(self, request):
#         return (datetime.date.today, datetime.date.today)
    
#     def get_rangefilter_created_at_title(self, request, field_path):
#         return 'save from dates'
    
#     def has_delete_permission(self, request, obj=None):
#         return False

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass