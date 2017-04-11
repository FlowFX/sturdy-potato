"""Views for the farms app."""

from django.views.generic import CreateView, DetailView

from .models import Address


class AddressDetailView(DetailView):
    pass


class AddressCreateView(CreateView):

    model = Address
    fields = ('street', 'postal_code', )
