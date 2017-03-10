"""Views for the potato project."""

from potatos.models import Potato

from django.views.generic import CreateView, DetailView, ListView, TemplateView


class IndexView(TemplateView):
    """Template view for the home page."""

    template_name = 'index.html'


class PotatoCreateView(CreateView):
    """Create view for the Potato model."""

    model = Potato
    fields = ['weight', 'variety']
    template_name = 'potatos/potato_form.html'


class PotatoDetailView(DetailView):
    """Detail view for the Potato object."""

    model = Potato
    context_object_name = 'potato'
    template_name = 'potatos/potato_detail.html'


class PotatoListView(ListView):
    """List view for the Potato object."""

    model = Potato
    context_object_name = 'potatos'
    template_name = 'potatos/potato_list.html'
