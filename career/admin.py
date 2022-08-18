from django.contrib import admin
from career.models import *
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html, urlencode
import csv
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
import datetime
from import_export.resources import ModelResource
from import_export.fields import Field
# Register your models here.

# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)
#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])
#         return response
#     export_as_csv.short_description = "Export Selected"

class ApplicationFormResource(ModelResource):
    resume_link = Field()
    class Meta:
        model = ApplicationForm
        export_order = ('id','full_name', 'email', 'contact','linkedin_link','designation','remarks', 'status', 'created_at', 'updated_at', 'is_deleted','resume_link')
    
    def dehydrate_resume_link(self, obj):
        url = obj.resume.url
        print(url)
        return url

@admin.register(ApplicationForm)
class ApplicationFormAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ApplicationFormResource
    list_display = ['full_name', 'email', 'contact','linkedin_link','designation','remarks', 'status', 'created_at', 'updated_at', 'is_deleted']
    list_filter  = ['designation','status', ('created_at', DateRangeFilter),]
    # actions      = ["export_as_csv"]
    # date_hierarchy = 'created_at'
    
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'save from dates you would like'

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

@admin.register(Career)
class CareerSummer(ImportExportModelAdmin, SummernoteModelAdmin):
    list_display = ('designation', 'priority', 'location', 'report_to','employee_type', 'created_at', 'updated_at', 'is_deleted', 'created_by')
    list_filter = ("location","report_to","employee_type")
    search_fields = ['location', 'report_to']
    summernote_fields = ('expect_from_you',"ideal_candidate","love_working_fpay","perks_benefits")
    readonly_fields     = ('created_by',)
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def save_model(self, request, obj, form, change):
        platform_user   = User.objects.get(username=request.user)

        obj.created_by  = platform_user
        obj.save()
