from faq.serializers import *
from faq.models import *

from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

import django_filters



class FaqListAPIView(APIView):

    def get(self, request, format=None):
        response = {}
        responsedata = []

        data = Faq.objects.all()

        if request.query_params.get('user_type'):
            data = data.filter(user_type=request.query_params.get('user_type'))

        data = data.order_by('priority')

        serializers = GetFaqListSerializer(data, many=True)

        responsedata.append('Faq Application Faq List Fetch SuccessFully.')
        response['success'] = True
        response['status'] = status.HTTP_200_OK
        response['message'] = responsedata
        response['data'] = serializers.data
        return Response(response)
