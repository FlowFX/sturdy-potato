from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PotatoListView.as_view(), name='list'),
    url(r'^new$', views.PotatoCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.PotatoDetailView.as_view(), name='detail'),
]
