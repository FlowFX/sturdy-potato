"""Views for the potato project."""

from potatos.models import Potato

from django.views.generic import DetailView, ListView, TemplateView


class IndexView(TemplateView):
    """View for the home page."""

    template_name = 'index.html'


class PotatoListView(ListView):
    """List view for all Potato objects."""

    model = Potato
    context_object_name = 'potatos'


class PotatoDetailView(DetailView):
    """Single object view for the Potato object."""

    model = Potato
    context_object_name = 'potato'
