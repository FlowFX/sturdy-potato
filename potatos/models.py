"""Django models for the potatos module."""

from django.db import models


class Potato(models.Model):
    """The Potato model."""

    weight = models.IntegerField()
    variety = models.CharField(max_length=255)
