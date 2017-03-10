"""Model factories for the potatoes project."""

from potatoes.models import Potato, SturdyPotato

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


class SturdyPotatoFactory(DjangoModelFactory):
    """ModelFactory for the Potato object."""

    class Meta:  # noqa
        model = SturdyPotato

    weight = FuzzyInteger(1, 1000)
    variety = FuzzyChoice(['Anya',
                           'Arran Victory',
                           'Blaue Viola',
                           'Doré',
                           'Duke of York',
                           ])
