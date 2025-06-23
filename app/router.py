from django.urls import path
from .controllers.product_controller import ProductController

urlpatterns = [
    path('api/products/', ProductController.as_view(), name='products-api'),
]