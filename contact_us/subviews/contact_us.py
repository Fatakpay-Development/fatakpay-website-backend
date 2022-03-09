from contact_us.serializers import *
from contact_us.models import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from fatakpay_cms.mail import custom_mail




class ContactUsListAPIView(APIView):

    def get(self, request, format=None):
        data = ContactUs.objects.filter(is_deleted=False)
        serializer = GetContactUsListSerializer(data, many=True)
        return Response({
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'ContactUs List Fetch SuccessFully',
            'data': serializer.data},
            status = status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostContactUsSerializer(data=request.data)
        if serializer.is_valid():
            email_id = serializer.validated_data.get('email')
            customer_name = serializer.validated_data.get('full_name')
            # if ContactUs.objects.filter(email = email_id).exists():
            #     return Response({
            #         'success': False,
            #         'status_code': status.HTTP_400_BAD_REQUEST,
            #         'message': 'Email Is All Ready Exist',
            #         'data': serializer.errors},
            #         status = status.HTTP_400_BAD_REQUEST)
            # else:
            Subject = "Thank you for getting in touch!"
            html_content = "<p>Hello {customer_name}, <br><br>We have received your message and would like to thank you for writing to us. One of our colleagues<br><br> will get back in touch with you soon! <br>If your inquiry is urgent, please call us on +91 8976226669 to talk to one of our staff members. <br><br> <br> Talk to you soon, <br> Team FatakPay</p>".format(customer_name = customer_name )
            Message = ""
            To = [email_id,]
            custom_mail(Subject, Message, To, html_content)
            serializer.save(email=email_id)
            # serializer.save()
            return Response({
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': 'ContactUs Data saved SuccessFully',
                'data': serializer.data},
                status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
