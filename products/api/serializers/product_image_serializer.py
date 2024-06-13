from rest_framework import serializers
from products.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    #
    # @staticmethod
    # def get_url(obj):
    #     return obj.image.url

    class Meta:
        model = ProductImage
        fields: tuple = 'title', 'image'
        ordering: list = 'row',

