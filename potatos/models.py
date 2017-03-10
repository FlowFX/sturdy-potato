"""Django models for the potatos module."""

from django.db import models


class Potato(models.Model):
    """The Potato model."""

    name = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
