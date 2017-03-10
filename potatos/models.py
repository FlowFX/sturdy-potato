"""Django models for the potatos module."""

from django.core import validators
from django.db import models
from django.urls import reverse


IsPositive = validators.MinValueValidator(1)


class Potato(models.Model):
    """The Potato model."""

    weight = models.IntegerField(validators=[IsPositive])
    variety = models.CharField(max_length=255)

    def get_absolute_url(self):
        """Return URL of the object's detail view."""
        return reverse('detail', args=[str(self.id)])
