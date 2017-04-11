"""Views for the farms app."""

from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView

from .forms import AddressForm
from .models import Address

from postalcodes_mexico import places


def get_places(request):

    if request.method == 'GET':
        postal_code = request.GET['postal_code']

    my_places = places(postal_code)
    my_places = [place._asdict() for place in my_places]

    return JsonResponse(my_places, safe=False)


class AddressDetailView(DetailView):
    pass


class AddressCreateView(CreateView):

    model = Address
    form_class = AddressForm
