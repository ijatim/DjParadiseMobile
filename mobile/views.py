from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Mobile, Record


class RecordsList(View):
    template = 'mobile/records_list.html'

    def get(self, request):
        available_r = Record.objects.filter(availability='AVAILABLE')
        sold_r = Record.objects.filter(availability='SOLD')

        return render(request, self.template, context={'available_r': available_r.all(), 'sold_r': sold_r.all()})


class RecordDetail(View):
    template = 'mobile/record_detail.html'

    def get(self, request, IMEI, pk):
        mobile_obj = get_object_or_404(Mobile, IMEI=IMEI)
        record_obj = get_object_or_404(Record, pk=pk, mobile=mobile_obj)

        return render(request, self.template, context={'record': record_obj})
