create-pypkg
============

Python Package Scaffold Builder

[![Test](https://github.com/dceoy/create-pypkg/actions/workflows/test.yml/badge.svg)](https://github.com/dceoy/create-pypkg/actions/workflows/test.yml)
[![Upload Python Package](https://github.com/dceoy/create-pypkg/actions/workflows/python-publish.yml/badge.svg)](https://github.com/dceoy/create-pypkg/actions/workflows/python-publish.yml)
[![CI to Docker Hub](https://github.com/dceoy/create-pypkg/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/dceoy/create-pypkg/actions/workflows/docker-publish.yml)

Installation
------------

```sh
$ pip install -U create-pypkg
```

Docker image
------------

The image is available at [Docker Hub](https://hub.docker.com/r/dceoy/create-pypkg/).

```sh
$ docker image pull dceoy/create-pypkg
```

Usage
-----

1.  Create a new package.

    Replace `newpackage` below with your package's name.

    ```sh
    $ mkdir newpackage
    $ create-pypkg ./newpackage
    ```

2.  Test the command-line interface of the package. (optional)

    ```sh
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -U ./newpackage
    $ newpackage --help
    $ newpackage --debug foo bar
    ```

Run `create-pypkg --help` for more information.
