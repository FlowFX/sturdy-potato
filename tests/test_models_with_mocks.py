"""Unit test the potatos models."""

from potatos.factories import PotatoFactory
from potatos.models import Potato

import pytest

from mock import patch, MagicMock


@patch('potatos.models.Potato.save', MagicMock(name="save"))
def test_save_with_mocked_save_method_does_not_generate_slug():
    # GIVEN a new Potato object
    potato = PotatoFactory.build()

    # WHEN saving the object
    potato.save()

    # THEN no slug is created, because the mocked 'save' method doesn't do anything
    assert potato.slug is ''


def no_test_save_generates_different_slug_for_every_object():
    # GIVEN a 2 new potatos, saved to the database
    potatos = PotatoFactory.create_batch(2)

    # THEN their slugs are different
    assert potatos[0].slug is not potatos[1].slug


# @patch('app.leaseagreements.models.LeaseAgreementHousing.super_save', MagicMock(name="super_save"))
# @pytest.mark.usefixtures('in_memory')
# class TestLeaseAgreementHousing:
#     """Collection of unit tests for the LeaseAgreementHousing model."""
#
#     def test_slug(self):
#         # GIVEN nothing
#         # WHEN creating a new lease agreements
#         b = LeaseAgreementHousing()
