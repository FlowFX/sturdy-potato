import json

from django.urls import reverse

from farms.factories import AddressFactory
from farms.views import AddressDetailView

import postalcodes_mexico

import pytest



class TestAddressViews:

    def test_detail_view(self, client, mocker):
        """Unit test for address detail view."""

        # GIVEN an address
        address = AddressFactory.build()
        mocker.patch.object(AddressDetailView, 'get_object', return_value=address)

        # WHEN requesting the DetailView
        url = reverse('farms:address_detail', kwargs={'pk': 1234})
        response = client.get(url)

        # THEN there is all the info we want
        content = response.content.decode()

        assert response.status_code == 200
        assert address.street in content
        assert address.postal_code in content
        assert address.city in content

    def test_create_view_GET_request(self, client):
        # GIVEN any state
        # WHEN requesting the create view for an address
        url = reverse('farms:address_create')
        response = client.get(url)

        # THEN there is a form and stuff
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_view_POST_request(self, client, mocker):
        # GIVEN any state
        # WHEN requesting the create view for an address
        url = reverse('farms:address_create')
        data = {
            'street': 'Bajío 296',
            'postal_code': '06760',
            'place': 'Roma Sur',
            'municipality': 'Alvaro Obregon',
            'city': 'Mérida',
            'state': 'Jalisco',
        }

        response = client.post(url, data=data)

        # THEN there is a form and stuff
        assert response.status_code == 302


def test_get_places_view(client):
    # GIVEN a Mexican postal code with one correcponding place
    postal_code = '01030'
    places = postalcodes_mexico.places(postal_code)

    place = places[0]

    # WHEN requesting the get_places view
    url = reverse('farms:address_get_places')
    response = client.get(url, {'postal_code': postal_code})

    data_json = response.content.decode()
    my_place = json.loads(data_json)

    # THEN the response contains a dictionary with all the places info
    assert type(my_place) == dict
    assert my_place.get('number_of_places') > 0

    assert my_place.get('city') == place.city
    assert my_place.get('municipality') == place.municipality
    assert my_place.get('state') == place.state
