from rest_framework import serializers
from products.models import Category


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields: tuple = 'title', 'keyword', 'description'

