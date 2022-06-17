from corporate.serializers import *
from corporate.models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from fatakpay_cms.mail import custom_mail

class CorporateAPIView(APIView):

    def post(self, request, format=None):
        serializer = PostCorporateSerializer(data=request.data)
        if serializer.is_valid():
            email_id = serializer.validated_data.get('work_email')
            # customer_name = serializer.validated_data.get('full_name')
                # if Corporate.objects.filter(work_email = email_id).exists():
                #     return Response({
                #         'success': False,
                #         'status_code': status.HTTP_400_BAD_REQUEST,
                #         'message': 'Email Is All Ready Exist',
                #         'data': serializer.errors},
                #         status = status.HTTP_400_BAD_REQUEST)
                # else:
            # Subject = "Welcome to FatakPay! We’re so glad you’re here"
            # html_content = "<p>Hello {customer_name}, <br><br>Thanks for joining the FatakPay list and showing interest in a demo! <br><br>We have been working really hard over the past three months developing the best FinTech platform<br> which will enable the masses to access quick and easy credit. <br><br><br>You've been added to our VIP list and will now be among the first to hear from us when we launch.<br><br><br>Talk to you soon,<br>Team FatakPay</p>".format(customer_name = customer_name )
            # Message = ""
            # To = [email_id,]
            # custom_mail(Subject, Message, To, html_content)
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
