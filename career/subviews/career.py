from career.serializers import *
from career.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size           = 1
    page_size_query_param = 'page_size'
    max_page_size       = 1

class GetCareerListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = Career.objects.all()
    serializer_class    = GetCareerListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostApplicationFormAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset            = ApplicationForm.objects.all()
    serializer_class    = PostApplicationFormSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
