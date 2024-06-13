from django.db import models
from django.utils.safestring import mark_safe


class ProductImage(models.Model):
    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images')
    title = models.CharField(max_length=50)
    row = models.PositiveIntegerField(default=1)

    def image_tag(self):
        if image := self.image:
            return mark_safe('<img src="{}" width="50px" height="50px" style="object-fit:cover;">'.format(image.url))
        return mark_safe('<span style="color:red">None</span>')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
