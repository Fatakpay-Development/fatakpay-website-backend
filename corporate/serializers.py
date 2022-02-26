from rest_framework import serializers
from rest_framework import fields
from corporate.models import *

class PostCorporateSerializer(serializers.ModelSerializer):
    full_name       = serializers.CharField(required=True)
    work_email      = serializers.CharField(required=True)
    company_name    = serializers.CharField(required=True)
    country_code    = serializers.CharField(required=True)
    contact         = serializers.CharField(required=True)

    class Meta:
        model = Corporate
        fields = ["full_name","work_email","company_name",'business_loc',"employee_no","where_hear","country_code", "contact",]

class GetCountryDialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryDialCode
        fields = ["name","dial_code","code"]