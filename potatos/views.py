"""Views for the potato project."""

from potatos.models import Potato

from django.views.generic import DetailView, TemplateView


class IndexView(TemplateView):
    """View for the home page."""

    template_name = 'index.html'


class PotatoDetailView(DetailView):
    """Single object view for the Potato object."""

    model = Potato
    context_object_name = 'potato'
