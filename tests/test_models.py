from potatos.models import Potato

import pytest


@pytest.mark.django_db
def test_save_and_retrieve_potato():
    """Test saving and retrieving Potato objects to and from the database."""

    # GIVEN an object and an empty database
    potato = Potato()
    potato.name = 'Hugo'
    potato.variety = 'Kennebec'
    assert Potato.objects.count() == 0

    # WHEN saving it to the database
    potato.save()

    # THEN it gets saved
    assert Potato.objects.count() == 1

    # AND can get retrived later
    new_potato = Potato.objects.first()

    assert new_potato.name == 'Hugo'
    assert new_potato.variety == 'Kennebec'

