from corporate.serializers import *
from corporate.models import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CorporateAPIView(APIView):

    def post(self, request, format=None):
        serializer = PostCorporateSerializer(data=request.data)
        if serializer.is_valid():
            email_id = serializer.validated_data.get('work_email')
            if Corporate.objects.filter(work_email = email_id).exists():
                return Response({
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': 'Email Is All Ready Exist',
                    'data': serializer.errors},
                    status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(email=email_id)
                return Response({
                    'success': True,
                    'status_code': status.HTTP_201_CREATED,
                    'message': 'Signup Data saved SuccessFully',
                    'data': serializer.data},
                    status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)