from django.db import models


class Product(models.Model):
    """Товар"""
    name = models.CharField('Название', max_length=255)

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Customer(models.Model):
    """Покупатель"""
    login = models.CharField('Логин', max_length=255)
    money_spent = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    stone = models.ManyToManyField(Product)

    objects = models.Manager

    def __str__(self):
        return self.login

    class Meta:
        ordering = ['money_spent']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class PurchaseHistory(models.Model):
    """Истрия Покупок"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.DecimalField("Сумма сделки", max_digits=9, decimal_places=2)
    quantity = models.DecimalField("Количество товара", max_digits=9, decimal_places=0)
    date = models.DateTimeField("Время")

    objects = models.Manager

    def __str__(self):
        return f"{self.customer.__str__()} - {self.item.__str__()}"

    class Meta:
        verbose_name = 'Истрия Покупок'
        verbose_name_plural = 'Истрии Покупок'

# Create your models here.
