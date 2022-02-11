from django.urls import path,include
from home_page.views import *
urlpatterns = [
    path('get_watch_video_list/', GetWatchVideoListAPIView.as_view()),
    path('post_signup/', PostSignUpAPIView.as_view()),
    path('get_testmonials_list/', GetTestmonialsListAPIView.as_view()),
]