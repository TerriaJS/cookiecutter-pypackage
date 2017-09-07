"""
Tests for `{{ cookiecutter.repo_name }}` module.
"""

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}

def test_is_positive(integers):
    result = {{ cookiecutter.repo_name }}.is_positive(integers)
    true_result = integers > 0
    assert (result == true_result)
