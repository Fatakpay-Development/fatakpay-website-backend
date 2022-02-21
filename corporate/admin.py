from django.contrib import admin
from .models import Corporate
# Register your models here.


@admin.register(Corporate)
class CorporateAdmin(admin.ModelAdmin):
    list_display        = ("full_name","work_email","company_name", "business_loc", "employee_no", "where_hear", "contact", "created_at","updated_at","is_deleted")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False