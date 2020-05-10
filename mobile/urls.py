from django.conf.urls import url
from .views import RecordDetail, RecordsList


urlpatterns = [
    url(r'^records/available/(?P<IMEI>\d+)/(?P<pk>\d+)/$', RecordDetail.as_view(), name='record_detail'),
    url(r'^records/$', RecordsList.as_view(), name='records_list')
]
