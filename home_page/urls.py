from django.urls import path,include
from home_page.views import *
urlpatterns = [
    path('v1/watch_video/', WatchVideoListAPIView.as_view()),
    path('v1/signup/', SignUpListAPIView.as_view()),
    path('v1/testmonials/', TestmonialsListAPIView.as_view()),
]