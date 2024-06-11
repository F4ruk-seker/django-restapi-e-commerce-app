from django.urls import path, include
from products.api.views import ProductListView, ProductDetailView


app_name: str = 'products'

urlpatterns: list[path] = [
    path('', ProductListView.as_view(), name='products'),
    path('<slug>', ProductDetailView.as_view(), name='product'),
]

