from contact_us.serializers import *
from contact_us.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView




class ContactUsListAPIView(APIView):

    def get(self, request, format=None):
        data = ContactUs.objects.all()
        serializer = GetContactUsListSerializer(data, many=True)
        return Response({
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'ContactUs List Fetch SuccessFully',
            'data': serializer.data},
            status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
