from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.


class User(ListAPIView):
    queryset = User.user_manager.all()
    serializer_class = UserSerializer
