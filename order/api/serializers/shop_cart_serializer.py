from rest_framework import serializers
from order.models import ShopCart
from order.api.serializers.shop_cart_product_serializer import ShopCartProductSerializer


class ShopCartSerializer(serializers.ModelSerializer):
    product = ShopCartProductSerializer()

    class Meta:
        model = ShopCart
        fields: tuple = 'product', 'quantity'

