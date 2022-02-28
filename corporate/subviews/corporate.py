from corporate.serializers import *
from corporate.models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CorporateAPIView(APIView):

    def post(self, request, format=None):
        serializer = PostCorporateSerializer(data=request.data)
        if serializer.is_valid():
            # email_id = serializer.validated_data.get('work_email')
            # if Corporate.objects.filter(work_email = email_id).exists():
            #     return Response({
            #         'success': False,
            #         'status_code': status.HTTP_400_BAD_REQUEST,
            #         'message': 'Email Is All Ready Exist',
            #         'data': serializer.errors},
            #         status = status.HTTP_400_BAD_REQUEST)
            # else:
                # Subject = 'here is mail from aniket',
                # Message = 'here is message from aniket',
                # To = [email_id]
                # custom_mail(Subject, Message, To)
            #     serializer.save(email=email_id)
            serializer.save()
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
