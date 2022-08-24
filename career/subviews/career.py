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
from fatakpay_cms.mail import custom_mail
logger = logging.getLogger('career')

class LargeResultsSetPagination(PageNumberPagination):
    page_size           = 1
    page_size_query_param = 'page_size'
    max_page_size       = 1


class CareerListAPIView(APIView):
    try:
        def get(self, request, format=None):
            data = Career.objects.filter(is_deleted=False)
            data = data.order_by('priority')
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


class CareerDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Career.objects.get(pk=pk)
        except Career.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = GetCareerListSerializer(data)
        return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'Job Detail Fetch SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_200_OK)

class ApplicationFormAPIView(APIView):

    def post(self, request, format=None):

        serializer = PostApplicationFormSerializer(data=request.data)
        if request.data['designation']:
            designation_obj = Career.objects.get(id=request.data['designation'])
            request.data['designation'] = designation_obj.id

        if serializer.is_valid():
            email_id = serializer.validated_data.get('email')
            customer_name = serializer.validated_data.get('full_name')
            designation = serializer.validated_data.get('designation')
            Subject = "Your application has been sent!"
            html_content = "<p>Hello {customer_name}, <br><br>We have received your application and would like to thank you for showing interest in a career with<br> FatakPay. One of our colleagues will get back in touch with you soon! <br><br><br> Talk to you soon, <br> Team FatakPay</p>".format(customer_name = customer_name )
            Message = ""
            To = [email_id,]
            custom_mail(Subject, Message, To, html_content, 'help@fatakpay.com')
            Hr_Subject = "CV received."
            Hr_to = ['jamir@fatakpay.com',]
            Hr_html_content = "<p>Hello HR, <br><br>You have received an application for {designation} from {customer_name}.".format(customer_name = customer_name, designation = designation )
            custom_mail(Hr_Subject, Message, Hr_to, Hr_html_content, 'help@fatakpay.com')
            serializer.save(status=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

