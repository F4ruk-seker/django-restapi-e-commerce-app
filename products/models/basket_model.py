from django.db import models


class BasketModel(models.Model):
    # user = OneToOne
    products = models.ManyToManyField('products.ProductModel', default=None, blank=True)

    def get_products(self):
        return self.products.all()

    def get_total_price(self):
        total_price = self.products.aggregate(total_price=models.Sum('price'))['total_price']
        return total_price or 0.0
