from django.contrib import admin
from home_page.models import *
# Register your models here.

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display        = ("full_name", "email","contact","created_at","updated_at","is_deleted")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

@admin.register(WatchVideo)
class WatchVideoAdmin(admin.ModelAdmin):
    list_display        = ("video", "created_at","updated_at","is_deleted","created_by")
    readonly_fields     = ('created_by',)

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


    def save_model(self, request, obj, form, change):
        platform_user   = User.objects.get(username=request.user)

        obj.created_by  = platform_user
        obj.save()


@admin.register(Testmonials)
class TestmonialsAdmin(admin.ModelAdmin):
    list_display        = ("full_name","designation","rating", "title", "description", "created_at","updated_at","is_deleted","created_by")
    readonly_fields     = ('created_by',)


    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def save_model(self, request, obj, form, change):
        platform_user   = User.objects.get(username=request.user)

        obj.created_by  = platform_user
        obj.save()

