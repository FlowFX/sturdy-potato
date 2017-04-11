"""Model factories for the farms app."""

from farms.models import Address

from factory.django import DjangoModelFactory


class AddressFactory(DjangoModelFactory):
    """ModelFactory for the Address object."""

    class Meta:  # noqa
        model = Address

    street = 'Calle Bajío 298, Interior 101'
    postal_code = '06760'  # a valid Mexican postal code
