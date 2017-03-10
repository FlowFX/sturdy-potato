from django.urls import reverse

from potatos.factories import PotatoFactory
from potatos.models import Potato

import pytest


slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)


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
    assert reverse('list') in content
    assert reverse('create') in content


@pytest.mark.django_db
def test_create_view_get_request(client):
    """Test the create view for a Potato object with the Django test client."""

    # GIVEN an empty database
    # WHEN doing a GET request to the Potato's create view
    url = reverse('create')
    response = client.get(url)

    # THEN it displays correctly
    assert response.status_code == 200


@slow
@pytest.mark.django_db
def test_create_view_post_request(client):
    """Test the create view for a Potato object with the Django test client."""

    # GIVEN an empty database
    # WHEN doing a POST request to the Potato's create view
    url = reverse('create')
    response = client.post(url, data={'weight': 100, 'variety': 'Ugly Cucumber',})

    # THEN it redirects to the new object's detail view
    assert response.status_code == 302
    assert response['location'] == '/potatos/1/'


@slow
@pytest.mark.django_db
def test_detail_view(client):
    """Test the detail view for a Potato object with the Django test client."""

    # GIVEN a Potato object in the database
    potato = PotatoFactory.create()

    # WHEN calling the DetailView for this object
    url = reverse('detail', kwargs={'pk': potato.id})
    response = client.get(url)

    content = response.content.decode()
    # THEN it shows the potato's ID and it's type
    assert response.status_code == 200
    assert str(potato.weight) in content
    assert potato.variety in content


@slow
@pytest.mark.django_db
def test_list_view(client):
    """Test the list view for Potato objects."""

    # GIVEN a number of potatos
    PotatoFactory.create_batch(5)

    # WHEN calling the list view for our potatos
    url = reverse('list')
    response = client.get(url)

    content = response.content.decode()
    # THEN all existing potatos are listed
    potatos = Potato.objects.all()

    for potato in potatos:
        assert str(potato.weight) in content
        assert potato.variety in content




