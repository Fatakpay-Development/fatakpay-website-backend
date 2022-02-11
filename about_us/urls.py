from django.urls import path

from about_us.views import *


urlpatterns = [
    
    path('get_about_us/',  GetAboutUsListAPIView.as_view()),
    path('retrieve_about_us_detail/<int:pk>', GetAboutUsDetailAPIView.as_view()),
]