from django.db import models

# Create your models here.

class PincodeCityState(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    pincode = models.IntegerField()
    town = models.CharField()
    city = models.CharField()
    state = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.pincode}|{self.city}|{self.state}"
