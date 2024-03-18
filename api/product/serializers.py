from rest_framework import serializers
from .models import Product
from api.category.serializers import *

class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    brand = BrandSerializer()
    gender = GenderSerializer()
    color = ColorSerializer()

    class Meta:
        model = Product
        fields = '__all__'
