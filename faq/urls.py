from django.urls import path

from faq.views import *


urlpatterns = [
    
    path('v1/faq/',  FaqListAPIView.as_view()),
    path('v1/faq-category-list/',  FaqCategoryListAPIView.as_view()),

]