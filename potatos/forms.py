"""Forms for the potatos project."""

from potatos.models import Potato
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit


from django import forms


class PotatoForm(forms.ModelForm):
    """ModelForm for the Potato model."""

    class Meta:  # noqa
        model = Potato
        fields = (
            'weight',
            'variety',
        )
