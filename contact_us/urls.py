from django.urls import path

from contact_us.views import *


urlpatterns = [
    
    path('get_contact_us_list/', GetContactUsListAPIView.as_view()),
    path('post_contact_us/', PostContactUsAPIView.as_view()),
]