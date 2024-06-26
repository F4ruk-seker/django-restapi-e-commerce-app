from django.contrib.auth.models import User
from django.db import models


class CommentModel(models.Model):
    class StatusType(models.TextChoices):
        HIDE = 'H', 'HIDE'
        ADMIN_HIDE = 'A', 'ADMIN_HIDE'
        SHOW = 'S', 'SHOW'

    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=0, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=10, choices=StatusType, default=StatusType.SHOW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_name_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
