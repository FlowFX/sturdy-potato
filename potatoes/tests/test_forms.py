"""Unit tests for the Potato form.

We use pytests parametrization to test our form for various input data.
Testing forms is especially important if custom validators are used
or custom clean_<fieldname> methods.

Testing the default Django forms functionality is redundant.

Here:
    weight = models.IntegerField(validators=[IsPositive])
    variety = models.CharField(max_length=255)
"""

from potatoes.forms import PotatoForm

import pytest


@pytest.mark.parametrize('weight, variety, validity',
                         [(100, 'Ugly Cucumber', True),
                          (0, 'Ugly Cucumber', False),    # Potato.weight >= 1 via model field validator
                          ('', '', False),                # Model fields are blank=False by default
                          ])
def test_potato_form(weight, variety, validity):
    # GIVEN test data and the PotatoForm
    # WHEN submitting the form with data
    form = PotatoForm(data={'weight': weight, 'variety': variety})

    # THEN it validates the data
    assert form.is_valid() is validity
