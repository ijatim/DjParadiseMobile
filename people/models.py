from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    identification_code = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.identification_code}'
