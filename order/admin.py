from django.contrib import admin
from order.models import Favorite, Order, OrderProduct, ShopCart


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display: tuple = 'product', 'user', 'quantity', 'price', 'amount'
    list_filter: list = 'user',


@admin.register(Favorite)
class FavoriteProductsAdmin(admin.ModelAdmin):
    list_display: tuple = 'product', 'user'
    list_filter: list = 'user',


class OrderProductLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields: tuple = 'user', 'product', 'price', 'quantity', 'amount'
    can_delete: bool = False
    extra: int = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display: list = 'first_name', 'last_name', 'city', 'total', 'status'
    list_filter: list = 'status',
    readonly_fields: tuple = 'user', 'address', 'city', 'country', 'first_name', 'ip', 'last_name', 'city', 'total'
    can_delete: bool = False
    inlines: list = OrderProductLine,


class OrderProductAdmin(admin.ModelAdmin):
    list_display: tuple = 'user', 'product', 'price', 'quantity', 'amount'
    list_filter: list = 'user',

