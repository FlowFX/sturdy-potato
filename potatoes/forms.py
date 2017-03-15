"""Forms for the potatoes project."""

from potatoes.models import Potato

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from django import forms


class PotatoForm(forms.ModelForm):
    """ModelForm for the Potato model."""

    class Meta:  # noqa
        model = Potato
        fields = (
            'weight',
            'variety',
        )

    def __init__(self, *args, **kwargs):
        """Initiate form with Crispy Form's FormHelper."""
        super(PotatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit(
            'cancel',
            'Cancel',
            css_class='btn-danger',
            formnovalidate='formnovalidate',
            )
        )