# pySchieber

[![Build Status](https://travis-ci.org/Ziegelstein/pySchieber.svg?branch=master)](https://travis-ci.org/Ziegelstein/pySchieber)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A tool to give runners an online presence. Check out the project's [documentation](http://Ziegelstein.github.io/pySchieber/).

A demp runs on the [soycaf.net](https://soycaf.net).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker-Compose]  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## TODO

- Setup a Helmchart
- Finalize the DB Structure
- Write Docs