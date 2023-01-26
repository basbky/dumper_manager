from typing import Type

from django.db import models


class Model(models.Model):
    """
    Represents a model of a dumper truck
    """

    name = models.CharField('Имя модели', max_length=255)
    load_capacity = models.IntegerField('Максимальная грузоподъёмность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель самосвала'
        verbose_name_plural = 'Модели самосвалов'


class Dumper(models.Model):
    """
    Represents a dumper truck
    """

    tail_number = models.CharField(max_length=255)
    model: Type[Model] = models.ForeignKey(Model, on_delete=models.CASCADE)
    load_weight = models.SmallIntegerField()

    def __str__(self):
        return self.tail_number

    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'
