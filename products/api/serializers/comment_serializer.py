from rest_framework import serializers
from products.models import CommentModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields: str = '__all__'
