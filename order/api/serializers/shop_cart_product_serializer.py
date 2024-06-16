from products.api.serializers.product_serializer import ProductSerializer
from products.models.product_model import ProductModel


class ShopCartProductSerializer(ProductSerializer):
    class Meta:
        model = ProductModel
        fields: tuple = 'image', 'name', 'price', 'slug'
