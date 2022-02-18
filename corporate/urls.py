from django.urls import path,include
from corporate.views import *
urlpatterns = [
    path('v1/corporate/', CorporateAPIView.as_view()),
]