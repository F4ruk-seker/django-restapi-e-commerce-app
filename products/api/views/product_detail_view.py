from rest_framework.generics import RetrieveAPIView
from products.api.serializers import ProductSerializer
from products.models import ProductModel


class ProductDetailView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field: str = 'slug'

