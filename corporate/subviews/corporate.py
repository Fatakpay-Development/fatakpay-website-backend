from corporate.serializers import *
from corporate.models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from fatakpay_cms.mail import custom_mail

class CorporateAPIView(APIView):

    def post(self, request, format=None):
        serializer = PostCorporateSerializer(data=request.data)
        if serializer.is_valid():
            email_id = serializer.validated_data.get('work_email')
            customer_name = serializer.validated_data.get('full_name')
            company = serializer.validated_data.get('company_name')
            location = serializer.validated_data.get('business_loc')
            mobile = serializer.validated_data.get('contact')
            numberOfEmp = serializer.validated_data.get('employee_no')
            if Corporate.objects.filter(work_email = email_id).exists():
                return Response({
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': email_id + ' is already registered with us.',
                    'data': serializer.errors},
                    status = status.HTTP_400_BAD_REQUEST)
            else:
                Subject = "Welcome to FatakPay! We’re so glad you’re here"
                html_content = """<p>Hi, <br><br>{customer_name} has shown interest in a demo of FatakPay and has shared their company details. Kindly call him/her and inquire.</p><br><br><table style="border: 1px solid black;"><tr>
                            <th style="border: 1px solid black;padding: 5px;">Full Name</th>
                            <td style="border: 1px solid black;padding: 5px;">{customer_name}</td>
                        </tr>
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Email Address</th>
                            <td style="border: 1px solid black;padding: 5px;">{email_id}</td>
                        </tr>
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Company Name</th>
                            <td style="border: 1px solid black;padding: 5px;">{company}</td>
                        </tr>
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Location</th>
                            <td style="border: 1px solid black;padding: 5px;">{location}</td>
                        </tr>
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Mobile No</th>
                            <td style="border: 1px solid black;padding: 5px;">{mobile}</td>
                        </tr>
                            <th style="border: 1px solid black;padding: 5px;">No. of Employee</th>
                            <td style="border: 1px solid black;padding: 5px;">{numberOfEmp}</td>
                        </tr>
                        </table>

                        <p>
                        <br><br><br>Regards,<br>Team FatakPay
                        </p>
                
                """.format(customer_name = customer_name, email_id = email_id, company = company, location = location, mobile = mobile, numberOfEmp = numberOfEmp )
                # html_content = "<p>Hi, <br><br>{customer_name} has shown interest in a demo of FatakPay and has shared their company details. Kindly call him/her and inquire.<br><br><br>Regards,<br>Team FatakPay</p>".format(customer_name = customer_name )
                Message = ""
                To = ['sales@fatakpay.com',]
                custom_mail(Subject, Message, To, html_content, 'help@fatakpay.com')
                serializer.save(work_email=email_id)
                # serializer.save()
                return Response({
                    'success': True,
                    'status_code': status.HTTP_201_CREATED,
                    'message': 'Signup Data saved SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

class CountryDialCodeAPIView(APIView):

    def get(self, request, format=None):
        response = {}
        responsedata = []

        data = CountryDialCode.objects.all()

        if request.query_params.get('name'):
            data = data.filter(name=request.query_params.get('name'))

        serializer = GetCountryDialCodeSerializer(data, many=True)

        responsedata.append('Country Dial Code List Fetch SuccessFully.')
        response['success'] = True
        response['status'] = status.HTTP_200_OK
        response['message'] = responsedata
        response['data'] = serializer.data
        return Response(response)



class ScheduleDemoAPIView(APIView):
    def post(self, request, format= None):
        serializer = ScheduleDemoSerializer(data= request.data)
        if serializer.is_valid():
            full_name = serializer.validated_data.get('full_name')
            email = serializer.validated_data.get('email')
            contact = serializer.validated_data.get('contact')
            comment = serializer.validated_data.get('comment')
            pricing = serializer.validated_data.get('pricing')
            if ScheduleDemo.objects.filter(email = email).exists():
                return Response({
                    'success' : False,
                    'status_code' : status.HTTP_400_BAD_REQUEST,
                    'message' : email + 'is already registerd with us',
                    'data' : serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                Subject = "Welcome to FatakPay! We’re so glad you’re here"
                html_content = """<p>Hi, <br><br>{full_name} has shown interest in a demo of FatakPay and has shared their details. Kindly call him/her and inquire.</p><br><br><table style="border: 1px solid black;"><tr>
                            <th style="border: 1px solid black;padding: 5px;">Full Name</th>
                            <td style="border: 1px solid black;padding: 5px;">{full_name}</td>
                        </tr>
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Email Address</th>
                            <td style="border: 1px solid black;padding: 5px;">{email}</td>
                        </tr>                       
                        <tr>
                            <th style="border: 1px solid black;padding: 5px;">Mobile No</th>
                            <td style="border: 1px solid black;padding: 5px;">{contact}</td>
                        </tr>
                            <th style="border: 1px solid black;padding: 5px;">Pricing</th>
                            <td style="border: 1px solid black;padding: 5px;">{pricing}</td>
                        </tr>
                        </table>

                        <p>
                        <br><br><br>Regards,<br>Team FatakPay
                        </p>
                
                """.format(full_name = full_name, email = email, contact = contact, pricing = pricing )
                # html_content = "<p>Hi, <br><br>{customer_name} has shown interest in a demo of FatakPay and has shared their company details. Kindly call him/her and inquire.<br><br><br>Regards,<br>Team FatakPay</p>".format(customer_name = customer_name )
                Message = ""
                To = ['sales@fatakpay.com',]
                custom_mail(Subject, Message, To, html_content, 'help@fatakpay.com')
                serializer.save(email = email)
                return Response({
                    'success' : True,
                    'status_code' : status.HTTP_201_CREATED,
                    'message' : 'Data saved successfully'
                }, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

