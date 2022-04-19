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