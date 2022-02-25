from django.urls import path,include
from corporate.views import *
urlpatterns = [
    path('v1/corporate/', CorporateAPIView.as_view()),
    path('v1/country_dial_code/', CountryDialCodeAPIView.as_view()),
]