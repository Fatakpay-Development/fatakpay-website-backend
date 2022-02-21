from rest_framework import serializers
from rest_framework import fields
from career.models import *

class GetCareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id','image', 'designation',"location","report_to","employee_type","expect_from_you","ideal_candidate","love_working_fpay","perks_benefits"]


class PostApplicationFormSerializer(serializers.ModelSerializer):
    full_name       = serializers.CharField(required=True)
    email           = serializers.CharField(required=True)
    contact         = serializers.CharField(required=True)
    resume          = serializers.FileField(required=True)
    
    class Meta:
        model = ApplicationForm
        fields = ['full_name', 'email','contact','linkedin_link','resume','designation']