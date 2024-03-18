from django.urls import path, include
from .views import *

urlpatterns = [
    path("category/", include("api.category.urls")),
    path("users/", include("api.users.urls")),
    path("products/", include("api.product.urls")),
    path("filter_master/", Filters.as_view({"get": "filters_master"})),
]
