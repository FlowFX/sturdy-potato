from django.db import models
from django.urls import reverse


class Address(models.Model):
    """An address model."""

    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=255)

    def get_absolute_url(self):
        """Return URL of the object's detail view."""
        return reverse('farms:address_detail', args=[str(self.id)])

