# Poetry Github CI/CD
A small project with a setup of CI/CD using Poetry. Using the actions [described by Jacob Kaplan-Moss](https://jacobian.org/til/github-actions-poetry/) as a starting point.

In this project I'm following the book [Hypermedia Systems](hypermedia.systems) about writing Hypermedia-Driven Applications with htmx. It's not a test driven project, it just happens to be the book I'm reading right now and I wanted a project to use in this repository.

Currently the integration consists in running PyTest and check the code format by using black.

Tests using PyTest are inside the 'tests' folder.


## Good to know
Poetry's configuration is local and can be read into the `poetry.toml` file.

Pyright's settings are defined inside the `[tool.pyright]` section of `pyproject.toml`.
