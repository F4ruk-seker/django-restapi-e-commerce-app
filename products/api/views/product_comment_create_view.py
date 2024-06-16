from rest_framework.generics import CreateAPIView
from products.models import CommentModel, ProductModel
from products.api.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE, HTTP_201_CREATED
from rest_framework.response import Response
# temp

from django.contrib.auth.models import User


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    model = CommentModel
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        def get_user():
            print(f'USER GEÇİCİ OLARAK ID1')
            return User.objects.first()

        if slug := kwargs.get(self.lookup_field):
            product = get_object_or_404(ProductModel, slug=slug)
            serializer: CommentSerializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                comment = CommentModel(**serializer.validated_data)
                comment.product = product
                # comment.user = request.user
                comment.user = get_user()
                comment.save()
                serializer = CommentSerializer(comment)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
            else:
                return Response(serializer.errors, HTTP_406_NOT_ACCEPTABLE)
