"""Views for the potato project."""

from potatos.models import Potato

from django.views.generic import CreateView, DetailView, ListView, TemplateView


class IndexView(TemplateView):
    """View for the home page."""

    template_name = 'index.html'


class PotatoCreateView(CreateView):

    model = Potato
    fields = ['weight', 'variety']

class PotatoDetailView(DetailView):
    """Single object view for the Potato object."""

    model = Potato
    context_object_name = 'potato'
    template_name = 'potatos/potato_detail.html'


class PotatoListView(ListView):
    """List view for all Potato objects."""

    model = Potato
    context_object_name = 'potatos'
    template_name = 'potatos/potato_list.html'

