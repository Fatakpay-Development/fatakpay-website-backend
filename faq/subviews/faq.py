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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Customer']

    def get(self, request, format=None):
        data = Faq.objects.all()
        serializer = GetFaqListSerializer(data, many=True)
        return Response({
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Faq Application Faq List Fetch SuccessFully',
                        'data': serializer.data},
                        status = status.HTTP_200_OK)