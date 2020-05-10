from django.contrib import admin
from .models import Model, Color, Brand, Mobile, Record, TestPaper, FactorPaper, PurchasePaper


admin.site.register(TestPaper)
admin.site.register(PurchasePaper)
admin.site.register(FactorPaper)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Mobile)
admin.site.register(Record)
