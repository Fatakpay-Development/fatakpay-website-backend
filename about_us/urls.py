from django.urls import path

from about_us.views import *


urlpatterns = [
    
    path('v1/about_us/',  AboutUsListAPIView.as_view()),
    path('v1/about_us/<int:pk>/', AboutUsDetailAPIView.as_view()),
]