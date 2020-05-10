from django.conf.urls import url
from .views import RecordDetail, RecordsList


urlpatterns = [
    url(r'^records/(?P<availability>\w+)/(?P<IMEI>\d+)/(?P<pk>\d+)/$', RecordDetail.as_view(),
        name='record_details'),
    url(r'^records/$', RecordsList.as_view(), name='records_list'),
]
