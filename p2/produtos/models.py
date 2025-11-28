from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.category}) - R$ {self.price}'
