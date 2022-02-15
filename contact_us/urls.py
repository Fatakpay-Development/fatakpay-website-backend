from django.urls import path

from contact_us.views import *


urlpatterns = [
    
    path('v1/contact_us/', ContactUsListAPIView.as_view()),
]
