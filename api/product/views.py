from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class ProductView(ViewSet):

    def get_products(self, request):
        request_body = request.data
        print(request)
        page = request_body["page"]
        limit = 18 * int(page)
        offset = limit - 18
        print(offset, limit)
        products = Product.objects.all()[offset:limit]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
