=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.png
    :target: http://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master

.. image:: https://pypip.in/d/{{ cookiecutter.repo_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}


{{ cookiecutter.project_short_description}}

{% if cookiecutter.use_eigen == 'yes' %}
Requirements
------------

* C++ compiler with C++11 support
* Eigen3
{% endif %}

Installation
------------

At the command line via pip in the project directory::

    $ pip install .

To install in develop mode with packages required for development::

    $ pip install -e .[dev]


Features
--------

* TODO
