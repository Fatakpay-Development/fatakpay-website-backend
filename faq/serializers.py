from rest_framework import serializers
from rest_framework import fields
from faq.models import *


class GetFaqListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['question','answer']