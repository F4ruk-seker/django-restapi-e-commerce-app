from django.contrib.auth.models import User
from django.db import models
from typing import Any
from random import randint
import string


class Order(models.Model):
    class StatusType(models.TextChoices):
        NEW = 'NEW', 'NEW'
        ACCEPTED = 'ACCEPTED', 'ACCEPTED'
        PREPARING = 'PREPARING', 'PREPARING'
        SHIPPING = 'SHIPPING', 'SHIPPING'
        COMPLETED = 'COMPLETED', 'COMPLETED'
        CANCELED = 'CANCELED', 'CANCELED'
        PENDING = 'PENDING', 'PENDING'
        APPROVED = 'APPROVED', 'APPROVED'
        REJECTED = 'REJECTED', 'REJECTED'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(max_length=5, editable=True)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=15, blank=True)
    # total = models.DecimalField(max_digits=10, decimal_places=)
    total = models.IntegerField()
    status = models.CharField(max_length=20, choices=StatusType, default=StatusType.NEW)
    ip = models.CharField(max_length=20, blank=True)
    admin_note = models.CharField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(string.ascii_lowercase[randint(0, 9)] for _ in range(5))
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.first_name} - {self.code}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('products.ProductModel', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.title


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('products.ProductModel', on_delete=models.SET_NULL, null=True)
    quantity: int = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return self.product.price

    @property
    def amount(self) -> Any:
        return self.quantity * self.product.price

    def increase(self):
        self.quantity += 1
        self.save()

    def decrease(self):
        self.quantity -= 1
        if self.quantity > 0:
            self.save()


class OrderProduct(models.Model):
    class StatusType(models.TextChoices):
        NEW = 'N', 'NEW'
        ACCEPTED = 'A', 'ACCEPTED'
        CANCELED = 'C', 'CANCELED'
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=StatusType, default=StatusType.NEW)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

