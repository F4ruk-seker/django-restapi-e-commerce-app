from django.urls import path, include


app_name: str = "api"

urlpatterns: list[path] = [
    path('payment/', include('payment.api.urls'), name='payment'),
    path('products/', include('products.api.urls'), name='products'),
    path('order/', include('order.api.urls'), name='order'),
]

