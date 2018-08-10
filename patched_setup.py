from unittest.mock import patch
from setuptools import setup

with open('../README.rst') as f:
    long_description = f.read()

original_setup = setup


def setup_wrap(*args, **kwargs):
    # Patch the project name and description
    kwargs.update({
        'name': 'coremltools_bdist_wininst',
        'long_description': long_description,
    })
    original_setup(*args, **kwargs)


@patch('setuptools.setup', wraps=setup_wrap)
def run_setup(mock_setup):
    import coremltools.setup

run_setup()
