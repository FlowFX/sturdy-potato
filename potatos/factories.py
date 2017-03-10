"""Model factories for the potatos project."""

from potatos.models import Potato

from factory.fuzzy import FuzzyChoice, FuzzyInteger
from factory.django import DjangoModelFactory


class PotatoFactory(DjangoModelFactory):
    """ModelFactory for the Potato object."""

    class Meta:  # noqa
        model = Potato

    weight = FuzzyInteger(1, 1000)
    variety = FuzzyChoice(['Anya',
                           'Arran Victory',
                           'Blaue Viola',
                           'Doré',
                           'Duke of York',
                           ])
