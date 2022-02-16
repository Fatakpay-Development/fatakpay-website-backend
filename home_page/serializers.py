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
    class Meta:
        model = SignUp
        fields = ['full_name', 'email','contact']

    def validate_contact(self, value):
        d = SignUp.objects.filter(contact=value).exists()
        if d == False:
            if value != "":
                return value
            raise serializers.ValidationError("Contact Is Required")
        raise serializers.ValidationError("Contact Is All Ready Exist")



class GetTestmonialsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonials
        fields = ['profile_image','full_name','designation','logo','rating','title','description']