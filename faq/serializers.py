# from importlib.resources import Resource
from rest_framework import serializers
from rest_framework import fields
from faq.models import *


class GetFaqListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['priority','user_type','question','answer','is_important']


class GetFaqCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqCategory
        fields = ['id', 'category']

class GetResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['video','priority','created_at','updated_at','is_deleted', 'created_by']