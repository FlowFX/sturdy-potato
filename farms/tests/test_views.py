from django.urls import reverse

from farms.factories import AddressFactory
from farms.views import AddressDetailView

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
