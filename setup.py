"""
Randomize test order plugin

The original source of the code is:

http://code.google.com/p/python-nose/issues/detail?id=255

and the original author is: Charles McCreary

"""
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='randomize',
    version='0.9',
    author='Nick Loadholtes',
    author_email='nick@ironboundsoftware.com',
    url='https://github.com/nloadholtes/nose-randomize',
    # original_author='Charles McCreary',
    # original_author_email = 'charles.mccreary@tiawichiresearch.com',
    description='Randomize the order of the tests within a unittest.TestCase class',
    license='GNU LGPL',
    py_modules=['randomize/plugin', 'randomize/__init__'],
    entry_points={
        'nose.plugins.0.10': [
            'randomize = randomize:Randomize'
            ]
        }
    )
