"""Django models for the potatos module."""

from django.db import models
from django.urls import reverse


class Potato(models.Model):
    """The Potato model."""

    weight = models.IntegerField()
    variety = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])