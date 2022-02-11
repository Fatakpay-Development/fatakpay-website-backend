from faq.serializers import *
from faq.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response


class GetFaqListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset            = Faq.objects.all()
    serializer_class    = GetFaqListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


