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
        data = {'street': 'Bajío 296', 'postal_code': '06760', 'city': 'Mérida'}

        response = client.post(url, data=data)

        # THEN there is a form and stuff
        assert response.status_code == 302


def test_get_places_view(client):
    # GIVEN a Mexican postal code with one correcponding place
    postal_code = '06760'
    place = postalcodes_mexico.places(postal_code)[0]

    # WHEN requesting the get_places view
    url = reverse('farms:address_get_places')
    response = client.get(url, {'postal_code': postal_code})

    data_json = response.content.decode()
    my_places = json.loads(data_json)

    # THEN the response contains a dictionary with all the places info
    assert len(my_places) == 1

    assert my_places[0].get('postal_code') == place.postal_code
    assert my_places[0].get('city') == place.city
    assert my_places[0].get('place') == place.place
    assert my_places[0].get('municipality') == place.municipality
    assert my_places[0].get('state') == place.state
