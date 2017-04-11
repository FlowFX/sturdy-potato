"""Views for the farms app."""

from django.views.generic import CreateView, DetailView

from .forms import AddressForm
from .models import Address


class AddressDetailView(DetailView):
    pass


class AddressCreateView(CreateView):

    model = Address
    form_class = AddressForm
