from django.contrib import admin
from career.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(ApplicationForm)

class careerSummer(SummernoteModelAdmin):
    list_display = ('designation', 'location', 'report_to','employee_type')
    list_filter = ("location","report_to","employee_type")
    search_fields = ['location', 'report_to']
    summernote_fields = ('expect_from_you',"ideal_candidate","love_working_fpay","perks_benefits")
    
admin.site.register(Career, careerSummer)
