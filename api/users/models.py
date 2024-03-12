from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from api.models import PincodeCityState
# Create your models here.


class UserManager(BaseUserManager):

    def create_superuser(
        self, email, username, mobile_no, first_name, last_name, password, **kwargs
    ):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_admin", True)

        self.create_user(
            email, username, mobile_no, first_name, last_name, password, **kwargs
        )

    def create_user(
        self, email, username, mobile_no, first_name, last_name, password=None, **kwargs
    ):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            mobile_no=mobile_no,
            first_name=first_name,
            last_name=last_name,
            **kwargs,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    email = models.CharField(blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    user_manager = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile_no", "username", "first_name", "last_name"]

    def __str__(self):
        return self.email


class UserAddress(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    address1 = models.CharField(max_length=200, null=False, blank=False)
    address2 = models.CharField(max_length=200, null=False, blank=False)
    address3 = models.CharField(max_length=200, null=True, blank=True)
    pincode_details = models.ForeignKey(PincodeCityState, on_delete=models.PROTECT, blank=False, default='000000')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
