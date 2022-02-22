from home_page.serializers import *
from home_page.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

class LargeResultsSetPagination(PageNumberPagination):
    page_size           = 1
    page_size_query_param = 'page_size'
    max_page_size       = 1

class WatchVideoListAPIView(APIView):

    def get(self, request, format=None):
        data = WatchVideo.objects.filter(is_deleted=False)
        serializer = GetWatchVideoListSerializer(data, many=True)
        return Response({
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Watchvideo List Fetch SuccessFully',
                        'data': serializer.data},
                        status = status.HTTP_200_OK)



class SignUpListAPIView(APIView):
    
    def post(self, request, format=None):
        serializer = PostSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TestmonialsListAPIView(APIView):

    def get(self, request, format=None):
        data = Testmonials.objects.filter(is_deleted=False)
        serializer = GetTestmonialsListSerializer(data, many=True)
        return Response({
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Testmonials List Fetch SuccessFully',
                        'data': serializer.data},
                        status = status.HTTP_200_OK)