"""
Randomize test order plugin
"""
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='Randomize test order plugin',
    version='0.2',
    author='Nick Loadholtes',
    author_email='nick@ironboundsoftware.com',
    # original_author='Charles McCreary',
    # original_author_email = 'charles.mccreary@tiawichiresearch.com',
    description = 'Randomize the order of the tests within a unittest.TestCase class',
    license = 'GNU LGPL',
    # py_modules = ['randomize'],
    entry_points = {
        'nose.plugins.0.10': [
            'randomize = randomize:Randomize'
            ]
        }

    )
