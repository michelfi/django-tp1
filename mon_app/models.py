from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)          # unique
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # prix précis
    stock = models.PositiveIntegerField(default=0)               # ≥ 0

    def __str__(self):
        return self.name
    