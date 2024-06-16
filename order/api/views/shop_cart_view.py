from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin
from order.models import ShopCart
from order.api.serializers import ShopCartSerializer


# temp

from django.contrib.auth.models import User


class ShopCartCreateListView(ListAPIView, CreateModelMixin):
    model = ShopCart
    serializer_class = ShopCartSerializer

    def get_queryset(self):
        def get_user():
            print(f'USER GEÇİCİ OLARAK ID1')
            return User.objects.first()

        return ShopCart.objects.filter(user=get_user()).all()


