from contact_us.serializers import *
from contact_us.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response


class GetContactUsListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = ContactUs.objects.all()
    serializer_class    = GetContactUsListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostContactUsAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset            = ContactUs.objects.all()
    serializer_class    = PostContactUsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
