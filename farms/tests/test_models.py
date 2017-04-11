"""Unit test the farms models."""

from ..factories import AddressFactory
from ..models import Address

import pytest


def test_address_factory_generates_valid_address():
    # GIVEN any state
    # WHEN building a new address
    address = AddressFactory.build()

    # THEN it has all the information we want
    assert address.street is not ''
    assert address.postal_code is not ''
    assert len(address.postal_code) == 5
    assert address.city is not ''


@pytest.mark.django_db
def test_address_can_be_saved_and_retrieved():
    # GIVEN a fresh address instance
    address = AddressFactory.build()
    street = address.street
    postal_code = address.postal_code

    # WHEN saving it to the database
    address.save()

    # THEN the db entry is correct
    saved_address = Address.objects.last()

    assert saved_address.street == street
    assert saved_address.postal_code == postal_code
