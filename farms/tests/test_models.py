"""Unit test the farms models."""

from farms.factories import AddressFactory

from mock import MagicMock


def test_address_factory_generates_valid_addresses_sort_of(mocker):
    """Same test, but using pytest-mock."""
    mocker.patch('farms.models.Address.save', MagicMock(name="save"))

    address = AddressFactory.create()

    assert address.street is not ''
    assert address.postal_code is not ''
    assert len(address.postal_code) == 5
    assert address.city is not ''
