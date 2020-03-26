from django.db import models

# Create your models here.

class ProductDetails(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_link = models.CharField(max_length=200) # upload image to elsewhere for this
    quantity = models.IntegerField(default=1, editable=False)

    class Meta:
        verbose_name_plural = "Product Details"

    def __str__(self):
        return self.name