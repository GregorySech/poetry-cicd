# Poetry Github CI/CD
A small project with a setup of CI/CD using Poetry. Using the actions [described by Jacob Kaplan-Moss](https://jacobian.org/til/github-actions-poetry/) as a starting point.

Tests using PyTest are inside the 'tests' folder.

In this project I'm following the book [Hypermedia Systems](hypermedia.systems) about writing Hypermedia-Driven Applications with htmx.

## Good to know
Poetry's configuration is local and can be read into the `poetry.toml` file.

Pyright's settings are defined inside the `[tool.pyright]` section of `pyproject.toml`.
