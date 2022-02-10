from about_us.serializers import *
from about_us.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response


class GetAboutUsListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = AboutUs.objects.all()
    serializer_class    = GetAboutUsListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetAboutUsDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset            = AboutUs.objects.all()
    serializer_class    = GetAboutUsDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
