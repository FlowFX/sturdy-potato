from django.urls import reverse

from potatoes.factories import PotatoFactory
from potatoes.models import Potato

import pytest


def test_index_view(client):
    """Test the index view using the Django test client."""

    # GIVEN the home page
    url = reverse('index')

    # WHEN calling it with the Django test client
    response = client.get(url)

    content = response.content.decode()
    # THEN it's there,
    assert response.status_code == 200
    # the project title is visible,
    assert '<h1>Sturdy Potato</h1>' in content
    # the correct template is used,
    assert 'index.html' in (template.name for template in response.templates)
    # and it links to the potato list view
    assert reverse('potatoes:list') in content
    assert reverse('potatoes:create') in content


@pytest.mark.django_db
def test_create_view_get_request(client):
    """Test the create view for a Potato object with the Django test client."""

    # GIVEN an empty database
    # WHEN doing a GET request to the Potato's create view
    url = reverse('potatoes:create')
    response = client.get(url)


    # THEN it displays correctly
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_view_post_request(client):
    """Test the create view for a Potato object with the Django test client."""

    # GIVEN an empty database
    # WHEN doing a POST request to the Potato's create view
    url = reverse('potatoes:create')
    response = client.post(url, data={'weight': 100, 'variety': 'Ugly Cucumber',})

    # THEN it redirects to the new object's detail view
    assert response.status_code == 302
    assert response['location'] == '/potatoes/1/'


@pytest.mark.django_db
def test_detail_view(client):
    """Test the detail view for a Potato object with the Django test client."""

    # GIVEN a Potato object in the database
    potato = PotatoFactory.create()

    # WHEN calling the DetailView for this object
    url = reverse('potatoes:detail', kwargs={'pk': potato.id})
    response = client.get(url)

    content = response.content.decode()
    # THEN it shows the potato's ID and it's type
    assert response.status_code == 200
    assert str(potato.weight) in content
    assert potato.variety in content


@pytest.mark.django_db
def test_list_view(client):
    """Test the list view for Potato objects."""

    # GIVEN a number of potatoes
    PotatoFactory.create_batch(5)

    # WHEN calling the list view for our potatoes
    url = reverse('potatoes:list')
    response = client.get(url)

    content = response.content.decode()
    # THEN all existing potatoes are listed
    potatoes = Potato.objects.all()

    for potato in potatoes:
        assert str(potato.weight) in content
        assert potato.variety in content
