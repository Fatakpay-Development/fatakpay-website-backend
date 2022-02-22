from about_us.serializers import *
from about_us.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

class AboutUsListAPIView(APIView):
            
    def get(self, request, format=None):
        data        = AboutUs.objects.filter(is_deleted=False)
        serializer  = GetAboutUsListSerializer(data, many=True)
        return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'AboutUs List Fetch SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_200_OK)




class AboutUsDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return AboutUs.objects.get(pk=pk)
        except AboutUs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = GetAboutUsDetailSerializer(data)
        return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'AboutUs Detail Fetch SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_200_OK)
    