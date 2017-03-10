"""Views for the potato project."""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Class-Based View for the home page."""

    template_name = 'index.html'
