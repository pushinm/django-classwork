from django.db import models


# Create your models here.


# TODO
# categories +
# seller
# product +


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=100)
    photo = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]


class Product(models.Model):
    CURRENCY_CHOICES = [
        ('UZS', "UZS"),
        ("USD", 'USD')
    ]

    name = models.CharField(verbose_name='Название продукта', max_length=100)
    price = models.IntegerField(verbose_name='Цена', choices=CURRENCY_CHOICES, default=CURRENCY_CHOICES[0])
    description = models.TextField('Описание')
    photo = models.ImageField(verbose_name='Фото продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
# seller = models.ForeignKey()

    def __str__(self) -> str:
        return f'{self.name} - {self.description[:20]}'