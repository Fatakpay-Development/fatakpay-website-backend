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
        data = ContactUs.objects.filter(is_deleted=False)
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
            # email_id = serializer.validated_data.get('email')
            # if ContactUs.objects.filter(email = email_id).exists():
            #     return Response({
            #         'success': False,
            #         'status_code': status.HTTP_400_BAD_REQUEST,
            #         'message': 'Email Is All Ready Exist',
            #         'data': serializer.errors},
            #         status = status.HTTP_400_BAD_REQUEST)
            # else:
            #     serializer.save(email=email_id)
            serializer.save()
            return Response({
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': 'Signup Data saved SuccessFully',
                'data': serializer.data},
                status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
