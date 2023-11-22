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
from fatakpay_cms.mail import custom_mail

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
            customer_name = serializer.validated_data.get('full_name')
            if SignUp.objects.filter(email = email_id).exists():
                return Response({
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': email_id + ' is already registered with us.',
                    'data': serializer.errors},
                    status = status.HTTP_400_BAD_REQUEST)
            else:
                Subject = "Welcome to FatakPay! We’re so glad you’re here"
                html_content = "<p>Hello {customer_name}, <br><br>Thanks for joining the FatakPay early access list! <br>We have been working really hard over the past three months developing the best FinTech platform<br> which will enable the masses to access quick and easy credit. <br>That's where you come in. If you have a minute, we'd appreciate a follow on LinkedIn! This helps us<br> get the word out, get feedback, and continue making FatakPay better. <br><br><strong>What's Next?</strong><br>When your invite is ready, we'll send you an email and SMS with a link to get started. Soon you'll get<br> a chance to try all the new features we've been building for FatakPay. <br><br><br>Regards,<br>Team FatakPay</p> <a href='https://fatakpay.com/'>Unsubscribe</a>".format(customer_name = customer_name )
                Message = ""
                To = ['sales@fatakpay.com',]
                custom_mail(Subject, Message, To, html_content, 'help@fatakpay.com')
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

class ReferCompanyAPIView(APIView):
    def post(self, request, format=None):
        serializer = PostReferCompanySerializer(data= request.data)
        if serializer.is_valid():
            customer_name = serializer.validated_data.get('manager_name')
            manager_email = serializer.validated_data.get('manager_email')
            company_name = serializer.validated_data.get('company_name')
            manager_mobile = serializer.validated_data.get('manager_mobile')
            numberOfEmp = serializer.validated_data.get('number_of_employees')
            if SignUp.objects.filter(email = manager_email).exists():
                return Response({
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': manager_email + ' is already registered with us.',
                    'data': serializer.errors},
                    status = status.HTTP_400_BAD_REQUEST)
            else:

                Subject = "Refer a company"
                html_content = """<p>Hi, <br><br>{company_name} has shown interest in a demo of FatakPay and has referred his/her HR manager. <br>Kindly call and inquire about his/her requirements.<br><br>
                <table style="border: 1px solid black;">
                    <tr>
                        <th style="border: 1px solid black;padding: 5px;">Full Name</th>
                        <td style="border: 1px solid black;padding: 5px;">{customer_name}</td>
                    </tr> 
                    <tr>
                        <th style="border: 1px solid black;padding: 5px;">Email Address</th>
                        <td style="border: 1px solid black;padding: 5px;">{manager_email}</td>
                    </tr>
                    <tr>
                        <th style="border: 1px solid black;padding: 5px;">Mobile No</th>
                        <td style="border: 1px solid black;padding: 5px;">{manager_mobile}</td>
                    </tr>
                    <tr>
                        <th style="border: 1px solid black;padding: 5px;">Company Name</th>
                        <td style="border: 1px solid black;padding: 5px;">{company_name}</td>
                    </tr>
                    <tr>
                        <th style="border: 1px solid black;padding: 5px;">No. of Employee</th>
                        <td style="border: 1px solid black;padding: 5px;">{numberOfEmp}</td>
                    </tr>
                </table>
                <br><br><br><br>Regards,<br>Team FatakPay</p>""".format(customer_name = customer_name, manager_email = manager_email, manager_mobile = manager_mobile, company_name = company_name, numberOfEmp = numberOfEmp )
                Message = ""
                To = ['sales@fatakpay.com',]
                custom_mail(Subject, Message, To, html_content, 'help@fatakpay.com')

                # mail to reefer
                # reeferSubject = "Welcome to FatakPay! We’re so glad you’re here"
                # reefer_html_content = "<p>Hi, <br><br>Thank you for showing interest and referring your HR manager/employer to us. <br>One of our team members will call him/her shortly.<br>If you have any further questions or concerns, please let us know. we&#39;re here to help!<br><br><br>Regards,<br>Team FatakPay</p>".format(company_name = company_name )
                # reeferTo = [manager_email,]
                # custom_mail(reeferSubject, Message, reeferTo, reefer_html_content, 'help@fatakpay.com')
                serializer.save()
                return Response({
                    'success': True,
                    'status_code': status.HTTP_201_CREATED,
                    'message': 'Refer Company Data saved SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)