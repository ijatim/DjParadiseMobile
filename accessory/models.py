from django.db import models
from django.core.validators import RegexValidator
from mobile.models import Model, Color


class BackCover(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class Glass(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class HandsFree(models.Model):
    # Choices
    handsfree_types = [('J Series', 'J Series'),]

    # Attributes
    type = models.CharField(max_length=10, choices=handsfree_types)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class AUXJack(models.Model):
    pass


class MobileCable(models.Model):
    pass


class MobileCharger(models.Model):
    pass


class CarCharger(models.Model):
    pass


class PowerBank(models.Model):
    pass


class WirelessCharger(models.Model):
    pass
