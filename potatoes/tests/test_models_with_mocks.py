"""Unit test the potatoes models."""

from farms.factories import AddressFactory
from potatoes.factories import PotatoFactory, SturdyPotatoFactory

from mock import patch, MagicMock


@patch('potatoes.models.Potato.save', MagicMock(name="save"))
def test_naively_mocked_save_method_does_not_generate_slug_at_all():
    # GIVEN a new Potato object
    potato = PotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN no slug is created, because the mocked 'save' method doesn't do anything
    assert potato.slug is ''


def test_naively_mocked_save_method_does_not_generate_slug_at_all_with_mocker(mocker):
    """Same test, but using pytest-mock."""
    mocker.patch('potatoes.models.Potato.save', MagicMock(name="save"))

    potato = PotatoFactory.build()
    assert potato.slug is ''

    potato.save()
    assert potato.slug is ''


@patch('potatoes.models.SturdyPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_slug():
    # GIVEN an enhanced Potato object
    potato = SturdyPotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN the slug is created, because the mocked 'super_save' method is super
    assert potato.slug is not ''


def test_properly_mocked_save_method_generates_slug_with_mocker(mocker):
    """Same test, but using pytest-mock."""
    mocker.patch('potatoes.models.SturdyPotato.super_save', MagicMock(name="super_save"))

    potato = SturdyPotatoFactory.build()
    assert potato.slug is ''

    potato.save()
    assert potato.slug is not ''


@patch('potatoes.models.SturdyPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_unique_slugs():
    # GIVEN a 2 new super potatoes, saved to the database
    potatoes = SturdyPotatoFactory.create_batch(2)

    # THEN their slugs are different
    assert potatoes[0].slug is not potatoes[1].slug


def test_properly_mocked_save_method_generates_unique_slugs_with_mocker(mocker):
    """Same test, but using pytest-mock."""
    mocker.patch('potatoes.models.SturdyPotato.super_save', MagicMock(name="super_save"))

    potatoes = SturdyPotatoFactory.create_batch(2)
    assert potatoes[0].slug is not potatoes[1].slug


def test_address_factory_generates_valid_addresses_sort_of(mocker):
    """Same test, but using pytest-mock."""
    mocker.patch('farms.models.Address.save', MagicMock(name="save"))

    address = AddressFactory.create()

    assert address.street is not ''
    assert address.postal_code is not ''
    assert len(address.postal_code) == 5
