from rest_framework import serializers
from rest_framework import fields
from about_us.models import *



class GetAboutUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['employee_name','designation','profile','description','employee_type','linkedin_link']


class GetAboutUsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['employee_name','designation','profile','description','employee_type','linkedin_link']
