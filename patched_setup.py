from unittest.mock import patch
from setuptools import setup

with open('../README.rst') as f:
    long_description = f.read()

original_setup = setup


def setup_wrap(*args, **kwargs):
    classifiers = [x for x in kwargs['classifiers']
                   if not x.startswith('Operating System :: ') and not x.startswith('Programming Language :: ')]
    classifiers.extend([
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ])

    # Patch the project name, description and classifiers
    kwargs.update({
        'name': 'coremltools_windows',
        'long_description': long_description,
        'classifiers': classifiers,
    })
    original_setup(*args, **kwargs)


@patch('setuptools.setup', wraps=setup_wrap)
def run_setup(mock_setup):
    import coremltools.setup

run_setup()
