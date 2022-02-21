from .models import *
from django.contrib import admin

# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display        = ("full_name", "email", "created_at","updated_at","is_deleted")

    def has_delete_permission(self, request, obj=None):
    # Disable delete
        return False
