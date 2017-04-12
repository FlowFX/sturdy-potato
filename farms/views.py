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
    # my_places = [place._asdict() for place in my_places]
    # place = my_places[0]

    response = {
        'postal_code': my_places[0].postal_code,
        'municipality': my_places[0].municipality,
        'city': my_places[0].city,
        'state': my_places[0].state,
        'place': my_places[0].place,
        'number_of_places': len(my_places),
    }

    return JsonResponse(response, safe=True)


class AddressDetailView(DetailView):

    model = Address


class AddressCreateView(CreateView):

    model = Address
    form_class = AddressForm
