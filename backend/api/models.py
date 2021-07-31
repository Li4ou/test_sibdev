from django.db import models


class PurchaseHistory(models.Model):
    """Истрия Покупок"""
    customer = models.CharField("Логин", max_length=255)
    item = models.CharField("Наименование", max_length=255)
    total = models.DecimalField("Сумма сделки", max_digits=9, decimal_places=2)
    quantity = models.DecimalField("Количество товара", max_digits=9, decimal_places=0)
    date = models.DateTimeField("Время")

    def __str__(self):
        return self.customer


# Create your models here.
