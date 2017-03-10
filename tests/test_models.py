"""Unit test the potatoes models."""

from potatoes.factories import PotatoFactory
from potatoes.models import Potato

import pytest


slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)


@slow
@pytest.mark.django_db
def test_save_and_retrieve_potato():
    """Test saving and retrieving Potato objects to and from the database."""

    # GIVEN an object and an empty database
    potato = PotatoFactory.build()
    assert Potato.objects.count() == 0

    # WHEN saving it to the database
    potato.save()

    # THEN it gets saved
    assert Potato.objects.count() == 1

    # AND can get retrieved later
    new_potato = Potato.objects.first()

    assert new_potato.weight == potato.weight
    assert new_potato.variety == potato.variety


@slow
@pytest.mark.django_db
def test_save_generates_random_slug():
    # GIVEN a new Potato object that has no slug yet
    potato = PotatoFactory.build()
    assert potato.slug is ''

    # WHEN saving the object
    potato.save()

    # THEN its slug is created
    assert potato.slug is not ''


@slow
@pytest.mark.django_db
def test_save_generates_different_slug_for_every_object():
    # GIVEN a 2 new potatoes, saved to the database
    potatoes = PotatoFactory.create_batch(2)

    # THEN their slugs are different
    assert potatoes[0].slug is not potatoes[1].slug
