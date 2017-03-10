"""Model factories for the potatos project."""

from potatos.models import Potato

from factory.fuzzy import FuzzyChoice
from factory import Sequence
from factory.django import DjangoModelFactory


class PotatoFactory(DjangoModelFactory):
    """ModelFactory for the Potato object."""

    class Meta:  # noqa
        model = Potato

    name = Sequence(lambda n: 'Oscar_%04d' % n)
    variety = FuzzyChoice(['Anya',
                           'Arran Victory',
                           'Blaue Viola',
                           'Doré',
                           'Duke of York',
                           ])
