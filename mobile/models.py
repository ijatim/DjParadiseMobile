from django.db import models
from people.models import Customer
from django.core.validators import RegexValidator


class Brand(models.Model):
    brand = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.brand.upper()}'


class Color(models.Model):
    color = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.color.title()}'


class Model(models.Model):
    # Choices
    attachment_choices = [('DUAL + SD CARD', 'DUAL + SD CARD'),
                          ('HYBRID', 'HYBRID'),
                          ('SINGLE + SD CARD', 'SINGLE + SD CARD'),
                          ('SINGLE', 'SINGLE'),
                          ('SD CARD', 'SD CARD'),
                          ('NO SIM', 'NO SIM')]

    storage_choices = [('4', '4GB'),
                       ('8', '8GB'),
                       ('16', '16GB'),
                       ('32', '32GB'),
                       ('64', '64GB'),
                       ('128', '128GB'),
                       ('256', '256GB'),
                       ('512', '512GB'),
                       ('1028', '1T')]

    ram_choices = [('1', '1GB'),
                   ('1.5', '1.5GB'),
                   ('1', '1GB'),
                   ('2', '2GB'),
                   ('3', '3GB'),
                   ('4', '4GB'),
                   ('6', '6GB'),
                   ('8', '8GB'),
                   ('12', '12GB')]

    # Attributes
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    ram = models.CharField(max_length=5, choices= ram_choices)
    storage = models.CharField(max_length=5, choices= storage_choices)
    attachments = models.CharField(max_length=16, choices=attachment_choices)

    def __str__(self):
        return f'{self.brand} {self.name} {self.color}: {self.storage}/{self.ram} - {self.attachments}'


class Mobile(models.Model):
    # Choices
    guarantee_choices = [('Yes', 'Yes'),
                         ('No', 'No')]

    registration_choices = [('OWN', 'OWN'),
                            ('POSTPONED', 'POSTPONED'),
                            ('WHITE', 'WHITE'),
                            ('NO', 'NO')]

    manufacturer_choices = [('China', 'China'),
                            ('India', 'India'),
                            ('Malaysia', 'Malaysia'),
                            ('Vietnam', 'Vietnam'),
                            ('United-State', 'United-State'),
                            ('Hong-Kong', 'Hong-Kong')]

    # Attributes
    IMEI = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,10}$')])
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    registration_status = models.CharField(max_length=10, choices=registration_choices)
    guarantee_status = models.CharField(max_length=3, choices=guarantee_choices)
    manufacturer = models.CharField(max_length=15, choices=manufacturer_choices)
    target_price = models.CharField('Target price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return f'{self.IMEI}:\n' \
               f'    {self.model}\n' \
               f'    {self.registration_status} - {self.guarantee_status}-{self.manufacturer}-{self.target_price}'


class PurchasePaper(models.Model):
    mobile = models.ForeignKey('Mobile', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    date = models.DateField()
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])


class TestPaper(models.Model):
    # Choices
    test_result_choices = [('PASSED', 'PASSED'), ('FAILED', 'FAILED')]

    # Attributes
    mobile = models.ForeignKey('Mobile', on_delete=models.CASCADE)
    page_number = models.IntegerField()
    date = models.DateField()
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    test_result = models.CharField(max_length=10, choices=test_result_choices)
    test_description = models.TextField()


class FactorPaper(models.Model):
    # Choices
    ownership_status_choices = [('OK', 'GIVEN'), ('NOT OK', 'NOT GIVEN')]

    # Attributes
    mobile = models.ForeignKey('Mobile', on_delete=models.CASCADE)
    factor_number = models.IntegerField()
    page_number = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.CharField('Price (1000T)', max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    ownership_status = models.CharField(max_length=10, choices=ownership_status_choices)


class Record(models.Model):
    # Choices
    sold_choices = [('AVAILABLE', 'AVAILABLE'),
                    ('SOLD', 'SOLD')]

    # Attribute
    availability = models.CharField(max_length=10, choices=sold_choices, default='AVAILABLE')
    mobile = models.ForeignKey('Mobile', on_delete=models.CASCADE)
    purchase_paper = models.ForeignKey('PurchasePaper', on_delete=models.CASCADE)
    test_paper = models.ForeignKey('TestPaper', on_delete=models.CASCADE)
    factor_paper = models.ForeignKey('FactorPaper', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.availability}: {self.mobile}'
