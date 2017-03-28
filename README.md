# sturdy-potato
[![Build Status](https://travis-ci.org/FlowFX/sturdy-potato.svg?branch=master)](https://travis-ci.org/FlowFX/sturdy-potato)
[![CircleCI](https://circleci.com/gh/FlowFX/sturdy-potato/tree/master.svg?style=svg)](https://circleci.com/gh/FlowFX/sturdy-potato/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/FlowFX/sturdy-potato/badge.svg?branch=master)](https://coveralls.io/github/FlowFX/sturdy-potato?branch=master)
[![Updates](https://pyup.io/repos/github/FlowFX/sturdy-potato/shield.svg)](https://pyup.io/repos/github/FlowFX/sturdy-potato/)

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
