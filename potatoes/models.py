"""Django models for the potatoes module."""

from .utils import random_key

from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Address(models.Model):
    """An address model."""

    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)


class Potato(models.Model):
    """The Potato model."""

    slug = models.SlugField(unique=True)
    weight = models.IntegerField(validators=[MinValueValidator(1)])
    variety = models.CharField(max_length=255)

    def get_absolute_url(self):
        """Return URL of the object's detail view."""
        return reverse('detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        """On save, create the object's slug if it doesn't exist yet."""
        if not self.slug:
            # Create unique slug
            self.slug = random_key(5)

        # Call the "real" save() method.
        super(Potato, self).save(*args, **kwargs)


class SturdyPotato(Potato):
    """A super potato."""

    def super_save(self, *args, **kwargs):
        """Call the 'real' save() method."""
        super(SturdyPotato, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """On save, create the object's slug if it doesn't exist yet."""
        if not self.slug:
            # Create unique slug on save
            self.slug = random_key(5)

        # Call the "real" save() method via a new super_save()
        self.super_save(*args, **kwargs)
