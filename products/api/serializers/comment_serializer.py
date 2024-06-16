from rest_framework import serializers
from products.models import CommentModel


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(required=False, read_only=True)

    @staticmethod
    def get_name(obj):
        if type(obj) is CommentModel:
            return obj.user.get_full_name() if not obj.is_name_hidden else (
                    f'{obj.user.first_name[0]}{'*'*5}{obj.user.first_name[-1]}'
                    ' '
                    f'{obj.user.last_name[0]}{'*'*5}{obj.user.last_name[-1]}'
                )

    class Meta:
        model = CommentModel
        fields: tuple = 'id', 'subject', 'comment', 'name', 'rate', 'is_name_hidden'
