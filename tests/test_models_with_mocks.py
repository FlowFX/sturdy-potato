"""Unit test the potatos models."""

from potatos.factories import PotatoFactory, SuperPotatoFactory

from mock import patch, MagicMock


@patch('potatos.models.Potato.save', MagicMock(name="save"))
def test_naively_mocked_save_method_does_not_generate_slug_at_all():
    # GIVEN a new Potato object
    potato = PotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN no slug is created, because the mocked 'save' method doesn't do anything
    assert potato.slug is ''


@patch('potatos.models.SuperPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_slug():
    # GIVEN a new Potato object
    potato = SuperPotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN no slug is created, because the mocked 'save' method doesn't do anything
    assert potato.slug is not ''


@patch('potatos.models.SuperPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_unique_slugs():
    # GIVEN a 2 new super potatos, saved to the database
    potatos = SuperPotatoFactory.create_batch(2)

    # THEN their slugs are different
    assert potatos[0].slug is not potatos[1].slug
