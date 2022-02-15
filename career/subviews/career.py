from career.serializers import *
from career.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from utils import custom_exceptions as ce
import logging
from rest_framework.views import APIView

logger = logging.getLogger('career')

class LargeResultsSetPagination(PageNumberPagination):
    page_size           = 1
    page_size_query_param = 'page_size'
    max_page_size       = 1


class CareerListAPIView(APIView):
    try:
        def get(self, request, format=None):
            data = Career.objects.all()
            serializer = GetCareerListSerializer(data, many=True)
            return Response({
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Career List Fetch SuccessFully',
                        'data': serializer.data},
                        status = status.HTTP_200_OK)

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


class ApplicationFormAPIView(APIView):

    def post(self, request, format=None):
        serializer = PostApplicationFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

