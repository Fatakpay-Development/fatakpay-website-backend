from django.urls import path,include
from career.views import *
urlpatterns = [
    path('get_career_list/', GetCareerListAPIView.as_view()),
    path('post_application_form/', PostApplicationFormAPIView.as_view()),
]