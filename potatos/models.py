"""Django models for the potatos module."""

from .utils import random_key

from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Potato(models.Model):
    """The Potato model."""

    slug = models.SlugField(unique=True)
    weight = models.IntegerField(validators=[MinValueValidator(1)])
    variety = models.CharField(max_length=255)

    def get_absolute_url(self):
        """Return URL of the object's detail view."""
        return reverse('detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.slug:
            # Create unique slug on save
            self.slug = random_key(5)

        super(Potato, self).save(*args, **kwargs)  # Call the "real" save() method.


class SuperPotato(Potato):
    """A super potato."""

    def super_save(self, *args, **kwargs):
        """Call the 'real' save() method."""
        super(SuperPotato, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Create unique slug on save
            self.slug = random_key(5)

        self.super_save(*args, **kwargs)
