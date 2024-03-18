from django.db import models

# Create your models here.


class Brands(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    brand = models.CharField(unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    category = models.CharField(unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Gender(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    gender = models.CharField(
        unique=True, choices=(("male", "Male"), ("female", "Female")), blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender


class Color(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    color = models.CharField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color
