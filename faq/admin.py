from .models import *
from django.contrib import admin

# Register your models here.

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display        = ("user_type", "question","answer","priority","is_important","created_at","updated_at","is_deleted","created_by")
    readonly_fields     = ('created_by',)

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def save_model(self, request, obj, form, change):
        platform_user   = User.objects.get(username=request.user)

        obj.created_by  = platform_user
        obj.save()
