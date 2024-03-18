from django.urls import path
from .views import *

urlpatterns = [
    path('',Category.as_view()),
    path('',Gender.as_view()),
    path('',Brand.as_view()),
    path('',Color.as_view()),
]
