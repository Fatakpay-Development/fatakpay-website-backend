from django.contrib import admin
from career.models import *
from django_summernote.admin import SummernoteModelAdmin
import csv
from django.http import HttpResponse
# Register your models here.

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"

@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('full_name', 'email', 'contact','linkedin_link','designation','remarks', 'status', 'created_at', 'updated_at', 'is_deleted')
    actions      = ["export_as_csv"]
    date_hierarchy = 'created_at'
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

@admin.register(Career)
class CareerSummer(SummernoteModelAdmin):
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
