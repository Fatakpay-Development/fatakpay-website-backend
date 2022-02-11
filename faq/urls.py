from django.urls import path

from faq.views import *


urlpatterns = [
    
    path('get_faq/',  GetFaqListAPIView.as_view()),
]