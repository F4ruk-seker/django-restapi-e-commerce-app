from django.urls import path
from order.api.views import ShopCartCreateListView


app_name: str = 'order'

urlpatterns: list[path] = [
    path('', ShopCartCreateListView.as_view(), name='shop_cart'),
]



