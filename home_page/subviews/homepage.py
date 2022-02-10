from home_page.serializers import *
from home_page.models import *

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

class GetWatchVideoListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = WatchVideo.objects.all()
    serializer_class    = GetWatchVideoListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostSingUpAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset            = SingUp.objects.all()
    serializer_class    = PostSingUpSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GetTestmonialsListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = Testmonials.objects.all()
    serializer_class    = GetTestmonialsListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)