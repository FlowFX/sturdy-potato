from django.db import models


class Address(models.Model):
    """An address model."""

    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)

