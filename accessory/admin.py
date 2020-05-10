from django.contrib import admin
from .models import (BackCover,
                     Glass,
                     HandsFree,
                     AUXJack,
                     MobileCable,
                     MobileCharger,
                     CarCharger,
                     PowerBank,
                     WirelessCharger)

admin.site.register(BackCover)
admin.site.register(Glass)
admin.site.register(HandsFree)
admin.site.register(AUXJack)
admin.site.register(MobileCharger)
admin.site.register(MobileCable)
admin.site.register(CarCharger)
admin.site.register(PowerBank)
admin.site.register(WirelessCharger)
