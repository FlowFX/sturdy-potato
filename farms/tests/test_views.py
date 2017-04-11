from django.urls import reverse

from farms.factories import AddressFactory
from farms.views import AddressDetailView


def test_address_detail_view(client, mocker):
    """Unit test for address detail view."""

    # GIVEN an address
    address = AddressFactory.build()
    mocker.patch.object(AddressDetailView, 'get_object', return_value=address)

    # WHEN requesting the DetailView
    url = reverse('address_detail', kwargs={'pk': 1234})
    response = client.get(url)

    # THEN there is all the info we want
    content = response.content.decode()

    assert response.status_code == 200
    assert address.street in content
    assert address.postal_code in content
