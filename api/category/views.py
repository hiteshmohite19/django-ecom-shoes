from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.


class Category(ListAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer


class Gender(ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class Color(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class Brand(ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
