from django.db import models
from api.category.models import *

# Create your models here.


class Product(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(unique=True, blank=False)
    description = models.TextField(blank=False)
    size_quantity = models.JSONField()
    price=models.DecimalField(decimal_places=2,blank=False, max_digits=10, default=499.00)
    brand = models.ForeignKey(Brands, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
