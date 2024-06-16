from django.db import models
from django.utils.safestring import mark_safe
from .product_image_model import ProductImage


class ProductModel(models.Model):
    class ItemType(models.TextChoices):
        PHYSICAL = 'P', 'PHYSICAL'
        VIRTUAL = 'v', 'VIRTUAL'

    class StatusType(models.TextChoices):
        DELETE = 'D', 'DELETE'
        HIDE = 'H', 'HIDE'
        SHOW = 'S', 'SHOW'

    name = models.CharField(max_length=50)
    item_type = models.CharField(max_length=1, default=ItemType.PHYSICAL, choices=ItemType)
    status = models.CharField(max_length=1, choices=StatusType, default=StatusType.SHOW)
    title = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='images/', blank=True)
    keyword = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    details = models.TextField(null=True, blank=True, default=None)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    # comments = models.ManyToManyField('products.CommentModel', default=None, blank=True, null=True)
    # comments =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)

    # def ra

    @property
    def image(self):
        return self.images_gallery[0]

    @property
    def images_gallery(self):
        return ProductImage.objects.filter(product=self).order_by('row')

    def image_tag(self):
        if image_model := self.image:
            return mark_safe(f'<img src="{image_model.image.url}" width="50px" height="50px" style="object-fit:cover">')
        else:
            return mark_safe('<span style="color:red">None</span>')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
