from typing_extensions import Required
from rest_framework import serializers
from rest_framework import fields
from home_page.models import *

class GetWatchVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchVideo
        fields = ['video']


class PostSignUpSerializer(serializers.ModelSerializer):
    full_name   = serializers.CharField(required=True)
    email       = serializers.CharField(required=True)
    country_code= serializers.CharField(required=True)

    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'country_code','contact']

class GetTestmonialsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonials
        fields = ['profile_image','full_name','designation','logo','rating','title','description']

class PostReferCompanySerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(required=True)
    manager_email = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)
    number_of_employees = serializers.IntegerField(required=True)

    class Meta:
        model = ReferCompany
        fields = ['manager_name','manager_email','company_name','number_of_employees']