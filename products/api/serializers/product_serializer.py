from rest_framework import serializers
from products.models import ProductModel
from products.api.serializers.product_image_serializer import ProductImageSerializer
from products.api.serializers.product_category_serializer import ProductCategorySerializer
from products.api.serializers.comment_serializer import CommentSerializer
from products.models.product_comment import CommentModel


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    category = ProductCategorySerializer()
    comments = serializers.SerializerMethodField()

    @staticmethod
    def get_comments(obj):
        return CommentSerializer(
            CommentModel.objects.filter(product=obj, status=CommentModel.StatusType.SHOW).all(),
            many=True
        ).data

    @staticmethod
    def get_image(obj):
        return ProductImageSerializer(obj.image).data

    @staticmethod
    def get_images(obj):
        return ProductImageSerializer(obj.images_gallery, many=True).data

    class Meta:
        model = ProductModel
        fields: str = '__all__'

