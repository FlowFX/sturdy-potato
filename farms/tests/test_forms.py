"""Unit tests for the Farms forms."""

from farms.forms import AddressForm

import pytest


TESTPARAMS = [
    ('Bajío 298', '06760', 'Cancun', True),
    ('Bajío 298', '06760', '', False),  # no empty fields
    ('', '', '', False),
]


@pytest.mark.parametrize('street, postal_code, city, validity', TESTPARAMS)
def test_address_form(street, postal_code, city, validity):
    # GIVEN test data and the AddressForm
    # WHEN submitting the form with data
    form = AddressForm(data={'street': street, 'postal_code': postal_code, 'city': city})

    # THEN it validates the data
    assert form.is_valid() is validity
