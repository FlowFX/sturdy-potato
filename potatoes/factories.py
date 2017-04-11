"""Model factories for the potatoes project."""

from potatoes.models import Address, Potato, SturdyPotato

from factory.fuzzy import FuzzyChoice, FuzzyInteger
from factory.django import DjangoModelFactory


class AddressFactory(DjangoModelFactory):
    """ModelFactory for the Address object."""

    class Meta:  # noqa
        model = Address

    street = 'Calle Bajío 298, Interior 101'
    postal_code = '06760'


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
