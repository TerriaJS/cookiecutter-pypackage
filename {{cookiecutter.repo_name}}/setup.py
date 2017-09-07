#!/usr/bin/env python
"""Setup environment for {{ cookiecutter.repo_name }}."""

from setuptools import setup, find_packages

exec(open('{{ cookiecutter.repo_name }}/__version__.py').read())
readme = open('README.md').read()

setup(
    name='{{ cookiecutter.repo_name }}',
    version=__version__,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/determinant-io/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.scripts.cli:cli',
        ]
    },
    install_requires=[
        'numpy==1.13.1',
        'scipy==0.19.1',
        'click==6.7',
        'mypy==0.521',
        'mypy_extensions==0.3.0'
    ],

    extras_require={
        'dev': [
            'pytest>=3.1.3',
            'pytest-flake8>=0.8.1',
            'pytest-mock>=1.6.2',
            'pytest-cov>=2.5.1',
            'pytest-regtest>=0.15.1',
            'flake8-docstrings>=1.1.0',
            'flake8-quotes>=0.11.0',
            'flake8-comprehensions>=1.4.1'
        ]
    },
    license="All Rights Reserved",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
