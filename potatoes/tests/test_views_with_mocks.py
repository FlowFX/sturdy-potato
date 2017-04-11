from django.urls import reverse

from potatoes.factories import PotatoFactory
from potatoes.views import PotatoDetailView, PotatoListView

from mock import patch


class TestPotatos:

    def test_detail_view(self, client):
        """Test the detail view for a Potato object with the Django test client."""
        # GIVEN a Potato object
        potato = PotatoFactory.build()  # This is not saved to the database

        """Here we monkey-patch the 'get_object" method of our DetailView.
        No matter with what kwargs we call the view, it will always use the
        'potato' object we pass as the 'return_value'. The view's original
        'get_object' is ignored. This means: no database call!
        """
        with patch.object(PotatoDetailView, 'get_object', return_value=potato):
            # WHEN calling the DetailView for this object
            url = reverse('potatoes:detail', kwargs={'pk': 1234})  # pk can be anything
            response = client.get(url)

            content = response.content.decode()
            # THEN it shows the potato's ID and it's type
            assert response.status_code == 200
            assert str(potato.weight) in content
            assert potato.variety in content

    def test_list_view(self, client):
        """Test the list view for Potato objects."""
        # GIVEN a number of potatoes
        potatoes = PotatoFactory.build_batch(5)

        """Same monkey-patching as above. For the ListView it is the 'get_queryset'
        method that we want to disable.
        """
        with patch.object(PotatoListView, 'get_queryset', return_value=potatoes):
            # WHEN calling the list view for our potatoes
            url = reverse('potatoes:list')
            response = client.get(url)

            content = response.content.decode()

            # THEN all existing potatos are listed
            for potato in potatoes:
                assert str(potato.weight) in content
                assert potato.variety in content

    def test_detail_view_with_mocker(self, client, mocker):
        """Same test, but using the mocker fixture from pytest-mock."""
        potato = PotatoFactory.build()

        # This is new
        mocker.patch.object(PotatoDetailView, 'get_object', return_value=potato)

        url = reverse('potatoes:detail', kwargs={'pk': 1234})
        response = client.get(url)

        content = response.content.decode()

        assert response.status_code == 200
        assert str(potato.weight) in content
        assert potato.variety in content

    def test_list_view_with_mocker(self, client, mocker):
        """Same test, but using the mocker fixture from pytest-mock."""
        potatoes = PotatoFactory.build_batch(5)

        # This is new
        mocker.patch.object(PotatoListView, 'get_queryset', return_value=potatoes)

        url = reverse('potatoes:list')
        response = client.get(url)

        content = response.content.decode()

        for potato in potatoes:
            assert str(potato.weight) in content
            assert potato.variety in content
