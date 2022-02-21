from django.contrib import admin
from career.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact','linkedin_link','designation', 'created_at', 'updated_at', 'is_deleted')

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

@admin.register(Career)
class CareerSummer(SummernoteModelAdmin):
    list_display = ('designation', 'location', 'report_to','employee_type', 'created_at', 'updated_at', 'is_deleted', 'created_by')
    list_filter = ("location","report_to","employee_type")
    search_fields = ['location', 'report_to']
    summernote_fields = ('expect_from_you',"ideal_candidate","love_working_fpay","perks_benefits")
    readonly_fields     = ('created_by',)
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def save_model(self, request, obj, form, change):
        platform_user   = User.objects.get(user=request.user)

        obj.created_by  = platform_user
        obj.save()
