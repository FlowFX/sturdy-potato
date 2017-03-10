# sturdy-potato
Django example code to support blog articles on flowfx.de


## Features
- pytest only
- view tests with the Django test client
- view tests that don't touch the database
- model tests
- model tests that don't touch the database

### pytest
- form tests with pytest parametrization
- pytest @slow marker to selectively runs slow tests

### Mocks
- mocks for DetailView.get_object
- mocks for ListView.get_queryset
- mocks for Model.save
