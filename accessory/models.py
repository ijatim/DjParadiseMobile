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
    handsfree_type_choices = [('J Series', 'J Series')]

    # Attributes
    type = models.CharField(max_length=10, choices=handsfree_type_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class AUXJack(models.Model):
    # Choices
    length_choices = [('1m', '1m'),
                      ('1.5m', '1.5m'),
                      ('2m', '2m')]

    # Attributes
    name = models.CharField(max_length=60)
    length = models.CharField(max_length=4, choices=length_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class MobileCable(models.Model):
    # Choices
    length_choices = [('1m', '1m'),
                      ('1.5m', '1.5m'),
                      ('2m', '2m'),
                      ('POWER BANK', 'POWER BANK')]

    model_choices = []

    cable_type_choices = [('Normal Charging', 'Normal Charging'),
                          ('Fast Charging', 'Fast Charging')]

    # Attributes
    model = models.CharField(max_length=20, choices=model_choices)
    cable_type = models.CharField(max_length=20, choices=cable_type_choices)
    length = models.CharField(max_length=10, choices=length_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class MobileCharger(models.Model):
    # Choices
    length_choices = [('1m', '1m'),
                      ('1.5m', '1.5m'),
                      ('2m', '2m')]

    ampere_choices = []
    material_choices = []

    # Attributes
    ampere = models.CharField(max_length=4, choices=ampere_choices)
    material = models.CharField(max_length=20, choices=material_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class CarCharger(models.Model):
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class PowerBank(models.Model):
    # Choices
    brand_choices = [('XIAOMI', 'XIAOMI'),
                     ('SAMSUNG', 'SAMSUNG')]

    capacity_choices = [('10000mA', '10000mA'),
                        ('20000mA', '20000mA')]

    # Attributes
    brand = models.CharField(max_length=15, choices=brand_choices)
    capacity = models.CharField(max_length=10, choices=capacity_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class WirelessCharger(models.Model):
    # Choices
    brand_choices = [('SAMSUNG', 'SAMSUNG')]

    capacity_choices = [('10000mA', '10000mA'),
                        ('20000mA', '20000mA')]

    # Attributes
    brand = models.CharField(max_length=15, choices=brand_choices)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
