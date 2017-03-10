from django.urls import reverse

from potatos.factories import PotatoFactory
from potatos.views import PotatoDetailView, PotatoListView

from mock import patch


def test_detail_view(client):
    """Test the detail view for a Potato object with the Django test client."""

    # GIVEN a Potato object
    potato = PotatoFactory.build()  # This is not saved to the database
    potato.id = 5                   # The ID is set when saving. We don't want that.

    """Here we monkey-patch the 'get_object" method of our DetailView.
    No matter with what kwargs we call the view, it will always use the
    'potato' object we pass as the 'return_value'. The view's original
    'get_object' is ignored. This means: no database call!
    """
    with patch.object(PotatoDetailView, 'get_object', return_value=potato):
        # WHEN calling the DetailView for this object
        url = reverse('detail', kwargs={'pk': 1234})  # pk can be anything
        response = client.get(url)

        content = response.content.decode()
        # THEN it shows the potato's ID and it's type
        assert response.status_code == 200
        assert str(potato.weight) in content
        assert potato.variety in content


def test_list_view(client):
    """Test the list view for Potato objects."""

    # GIVEN a number of potatos
    potatos = PotatoFactory.build_batch(5)

    """Same monkey-patching as above. For the ListView it is the 'get_queryset'
    method that we want to disable.
    """
    with patch.object(PotatoListView, 'get_queryset', return_value=potatos):
        # WHEN calling the list view for our potatos
        url = reverse('list')
        response = client.get(url)

        content = response.content.decode()

        # THEN all existing potatos are listed
        for potato in potatos:
            assert str(potato.weight) in content
            assert potato.variety in content

