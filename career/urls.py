from django.urls import path,include
from career.views import *
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views.decorators.clickjacking import xframe_options_sameorigin


urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/admin/')),
    path('grappelli/', include('grappelli.urls')),
    re_path(r'^admin/', admin.site.urls),
    path('v1/career/', CareerListAPIView.as_view()),
    path('v1/career/<int:pk>/', CareerDetailAPIView.as_view()),
    path('v1/application_form/', ApplicationFormAPIView.as_view()),
]