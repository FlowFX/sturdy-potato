from django.urls import reverse


def test_index_view(client):
    """Test the index view using the Django test client."""

    # GIVEN the home page
    url = reverse('index')

    # WHEN calling it with the Django test client
    response = client.get(url)

    # THEN it's there,
    assert response.status_code == 200
    # the project title is visible,
    assert '<h1>Sturdy Potato</h1>' in response.content.decode()
    # and the correct template is used
    assert 'index.html' in (template.name for template in response.templates)
