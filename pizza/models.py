from django.db import models
from django.forms import CharField


class Topping(models.Model):
    name = models.CharField(("トッピング名"), max_length=50)
    price = models.IntegerField('値段')
    outline = models.TextField('説明', )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'topping'
        verbose_name = 'トッピング'
        verbose_name_plural = 'トッピング'


class Pizza(models.Model):
    PIZZA_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    name = models.CharField(("ピザ名"), max_length=50)
    toppings = models.ManyToManyField(
        Topping, verbose_name=("トッピング"))
    size = models.CharField(
        'サイズ', max_length=50, choices=PIZZA_SIZES, default=PIZZA_SIZES[1], blank=True)
    price = models.IntegerField('値段')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pizza'
        verbose_name = 'ピザ'
        verbose_name_plural = 'ピザ'
