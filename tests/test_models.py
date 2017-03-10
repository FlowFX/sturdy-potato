"""Unit test the potatos models."""

from potatos.factories import PotatoFactory
from potatos.models import Potato

import pytest


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

