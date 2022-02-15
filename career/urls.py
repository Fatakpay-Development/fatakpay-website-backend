from django.urls import path,include
from career.views import *
urlpatterns = [
    path('v1/career/', CareerListAPIView.as_view()),
    path('v1/application_form/', ApplicationFormAPIView.as_view()),
]