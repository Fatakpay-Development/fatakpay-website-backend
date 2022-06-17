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
# from fatakpay_cms.mail import custom_mail

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
            email_id = serializer.validated_data.get('email')
            # customer_name = serializer.validated_data.get('full_name')
                # if SignUp.objects.filter(email = email_id).exists():
                #     return Response({
                #         'success': False,
                #         'status_code': status.HTTP_400_BAD_REQUEST,
                #         'message': 'Email Is All Ready Exist',
                #         'data': serializer.errors},
                #         status = status.HTTP_400_BAD_REQUEST)
                # else:
            # Subject = "Welcome to FatakPay! We’re so glad you’re here"
            # html_content = "<p>Hello {customer_name}, <br><br>Thanks for joining the FatakPay early access list! <br><br>We have been working really hard over the past three months developing the best FinTech platform<br> which will enable the masses to access quick and easy credit. <br><br>That's where you come in. If you have a minute, we'd appreciate a follow on LinkedIn! This helps us<br> get the word out, get feedback, and continue making FatakPay better. <br><br><br><strong>What's Next?</strong><br>When your invite is ready, we'll send you an email and SMS with a link to get started. Soon you'll get<br> a chance to try all the new features we've been building for FatakPay. <br><br><br>Regards,<br>Team FatakPay</p>".format(customer_name = customer_name )
            # Message = ""
            # To = [email_id,]
            # custom_mail(Subject, Message, To, html_content)
            serializer.save(email=email_id)
            # serializer.save()
            return Response({
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': 'Signup Data saved SuccessFully',
                'data': serializer.data},
                status = status.HTTP_201_CREATED) 
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