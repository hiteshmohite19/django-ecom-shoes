from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.category.models import *
from api.category.serializers import *
# Create your views here.

class Filters(ViewSet):

    def filters_master(self, request):
        gender = Gender.objects.only("id", "gender")
        gender_serializer = GenderSerializer(gender, many=True)
        brands = Brands.objects.only("id", "brand")
        brands_serializer = BrandSerializer(brands, many=True)
        category = Category.objects.only("id", "category")
        category_serializer = CategorySerializer(category, many=True)
        color = Color.objects.only("id", "color")
        color_serializer = ColorSerializer(color, many=True)

        resp = {
            'gender':gender_serializer.data,
            'brands':brands_serializer.data,
            'category':category_serializer.data,
            'color':color_serializer.data
        }

        return Response(resp)
