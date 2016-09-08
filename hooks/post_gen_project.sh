#!/bin/sh
{% if cookiecutter.use_eigen == "yes" %}
wget "http://bitbucket.org/eigen/eigen/get/3.2.9.tar.gz"
tar -xzf "3.2.9.tar.gz"
rm "3.2.9.tar.gz"
mv eigen-eigen-dc6cfdf9bcec eigen3
{% endif %}
