"""Unit test the potatoes models."""

from potatoes.factories import PotatoFactory, SuperPotatoFactory

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


@patch('potatoes.models.SuperPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_slug():
    # GIVEN an enhanced Potato object
    potato = SuperPotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN the slug is created, because the mocked 'super_save' method is super
    assert potato.slug is not ''


@patch('potatoes.models.SuperPotato.super_save', MagicMock(name="super_save"))
def test_properly_mocked_save_method_generates_unique_slugs():
    # GIVEN a 2 new super potatoes, saved to the database
    potatoes = SuperPotatoFactory.create_batch(2)

    # THEN their slugs are different
    assert potatoes[0].slug is not potatoes[1].slug
