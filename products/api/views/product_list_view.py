from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from products.api.serializers import ProductSerializer
from products.models import ProductModel


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    filter_backends = SearchFilter, OrderingFilter


