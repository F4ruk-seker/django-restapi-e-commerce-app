from rest_framework import serializers
from products.models import ProductModel
from products.api.serializers.product_image_serializer import ProductImageSerializer
from products.api.serializers.product_category_serializer import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    category = ProductCategorySerializer()

    @staticmethod
    def get_image(obj):
        return ProductImageSerializer(obj.image).data

    @staticmethod
    def get_images(obj):
        return ProductImageSerializer(obj.images_gallery.order_by('row'), many=True).data

    class Meta:
        model = ProductModel
        fields: str = '__all__'

