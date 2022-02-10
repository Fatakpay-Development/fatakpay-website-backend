from career.serializers import *
from career.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from utils import custom_exceptions as ce
import logging

logger = logging.getLogger('career')

class LargeResultsSetPagination(PageNumberPagination):
    page_size           = 1
    page_size_query_param = 'page_size'
    max_page_size       = 1

class GetCareerListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    try:
        queryset            = Career.objects.all()
        serializer_class    = GetCareerListSerializer
        
        print(hey)

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
    except NameError as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.NameErrorCe

    except AttributeError as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.AttributeErrorCe

    except KeyError as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.KeyErrorCe

    except UnboundLocalError as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.UnknownColumnError

    except IndexError as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.IndexErrorCe

    except Exception as e:
        logger.error('GET CAREER API VIEW : {}'.format( e))
        raise ce.InternalServerError


class PostApplicationFormAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset            = ApplicationForm.objects.all()
    serializer_class    = PostApplicationFormSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
