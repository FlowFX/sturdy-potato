"""Views for the potato project."""

from django.http import HttpResponseRedirect
from django.urls import reverse

from potatoes.models import Potato
from potatoes.forms import PotatoForm

from django.views.generic import CreateView, DetailView, ListView, TemplateView


class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if 'cancel' in request.POST:
            url = reverse('index')
            return HttpResponseRedirect(url)
        else:
            return super(FormActionMixin, self).post(request, *args, **kwargs)


class IndexView(TemplateView):
    """Template view for the home page."""

    template_name = 'index.html'


class PotatoCreateView(FormActionMixin, CreateView):
    """Create view for the Potato model."""

    model = Potato
    form_class = PotatoForm
    template_name = 'potatoes/potato_form.html'


class PotatoDetailView(DetailView):
    """Detail view for the Potato object."""

    model = Potato
    context_object_name = 'potato'
    template_name = 'potatoes/potato_detail.html'


class PotatoListView(ListView):
    """List view for the Potato object."""

    model = Potato
    context_object_name = 'potatoes'
    template_name = 'potatoes/potato_list.html'
