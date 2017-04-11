"""sturdy_potato URL Configuration."""
from django.conf.urls import include, url

from potatoes import views as potatoes_views


urlpatterns = [
    url(r'^$', potatoes_views.IndexView.as_view(), name='index'),
    url(r'^farms/', include('farms.urls', namespace='farms')),
    url(r'^potatoes/', include('potatoes.urls', namespace='potatoes')),
]
