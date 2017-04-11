from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^addresses/(?P<pk>[0-9]+)/$', views.AddressDetailView.as_view(), name='address_detail'),
]
