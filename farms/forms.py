"""Forms for the farms app."""

from .models import Address

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Button, Field, Fieldset, Submit


from django import forms


class AddressForm(forms.ModelForm):
    """ModelForm for the Address model."""

    class Meta:  # noqa
        model = Address
        fields = (
            'street',
            'postal_code',
            'place',
            'municipality',
            'city',
            'state',
        )
        widgets = {
            'place': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        """Initiate form with Crispy Form's FormHelper."""
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            Fieldset(
                'An address',
                Field(
                    'street',
                    autofocus=True,
                ),
                'postal_code',
                Field('place', placeholder='Wait for it.'),
                Field('municipality', readonly='true', placeholder='Will be filled automatically.'),
                Field('city', readonly='true', placeholder='Will be filled automatically.'),
                Field('state', readonly='true', placeholder='Will be filled automatically.'),
            ),
        )

        self.fields['place'].required = True
        self.fields['street'].required = True
        self.fields['postal_code'].required = True
