from rest_framework import serializers
from products.models import ProductModel
from products.api.serializers.product_image_serializer import ProductImageSerializer
from products.api.serializers.product_category_serializer import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = ProductCategorySerializer()

    def get_images(self, obj):
        return ProductImageSerializer(obj.images_gallery, many=True).data

    class Meta:
        model = ProductModel
        fields: str = '__all__'

