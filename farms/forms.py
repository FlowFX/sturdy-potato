"""Forms for the farms app."""

from .models import Address

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit


from django import forms


class AddressForm(forms.ModelForm):
    """ModelForm for the Address model."""

    class Meta:  # noqa
        model = Address
        fields = (
            'street',
            'postal_code',
            'city',
        )

    def __init__(self, *args, **kwargs):
        """Initiate form with Crispy Form's FormHelper."""
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Button(
            'complete',
            'Complete address',
            css_class='btn-success',
        ))
