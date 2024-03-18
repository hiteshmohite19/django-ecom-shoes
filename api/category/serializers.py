from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        exclude = ("created", "updated")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("created", "updated")


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        exclude = ("created", "updated")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ("created", "updated")
