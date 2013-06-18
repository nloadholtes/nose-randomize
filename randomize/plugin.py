"""
This plugin randomizes the order of tests within a unittest.TestCase class

The original source of the code is:

http://code.google.com/p/python-nose/issues/detail?id=255

and the original author is: Charles McCreary

"""
__test__ = False

import logging
from nose.plugins import Plugin
from nose import loader
from inspect import isfunction, ismethod
from nose.case import FunctionTestCase, MethodTestCase
from nose.failure import Failure
from nose.util import isclass, isgenerator, transplant_func, transplant_class
import random
import unittest

log = logging.getLogger(__name__)


class Randomize(Plugin):
    """
    Randomize the order of the tests within a unittest.TestCase class
    """
    name = 'randomize'
    # Generate a seed for deterministic behaviour
    # Could use getstate  and setstate, but that would involve
    # pickling the state and storing it somewhere. too lazy.
    seed = random.getrandbits(32)

    def options(self, parser, env):
        """Register commandline options.
        """
        Plugin.options(self, parser, env)
        parser.add_option('--randomize', action='store_true', dest='randomize',
                          help="Randomize the order of the tests within a unittest.TestCase class")
        parser.add_option('--seed', action='store', dest='seed', default=None, type=long,
                          help="Initialize the seed for deterministic behavior in reproducing failed tests")

    def configure(self, options, conf):
        """
        Configure plugin.
        """
        Plugin.configure(self, options, conf)
        if options.randomize:
            self.enabled = True
            if options.seed is not None:
                self.seed = options.seed
            random.seed(self.seed)
            print("Using %d as seed" % (self.seed,))

    def makeTest(self, obj, parent=None):
        """Given a test object and its parent, return a test case
        or test suite.
        """
        ldr = loader.TestLoader()
        if isinstance(obj, unittest.TestCase):
            return obj
        elif isclass(obj):
            if parent and obj.__module__ != parent.__name__:
                obj = transplant_class(obj, parent.__name__)
            if issubclass(obj, unittest.TestCase):
                # Randomize the order of the tests in the TestCase
                return self.Randomized_loadTestsFromTestCase(obj)
            else:
                return ldr.loadTestsFromTestClass(obj)
        elif ismethod(obj):
            if parent is None:
                parent = obj.__class__
            if issubclass(parent, unittest.TestCase):
                return parent(obj.__name__)
            else:
                if isgenerator(obj):
                    return ldr.loadTestsFromGeneratorMethod(obj, parent)
                else:
                    return MethodTestCase(obj)
        elif isfunction(obj):
            if parent and obj.__module__ != parent.__name__:
                obj = transplant_func(obj, parent.__name__)
            if isgenerator(obj):
                return ldr.loadTestsFromGenerator(obj, parent)
            else:
                return FunctionTestCase(obj)
        else:
            return Failure(TypeError,
                           "Can't make a test from %s" % obj)

    def Randomized_loadTestsFromTestCase(self, testCaseClass):
        l = loader.TestLoader()
        tmp = l.loadTestsFromTestCase(testCaseClass)
        randomized_tests = []
        for t in tmp._tests:
            randomized_tests.append(t)
        random.shuffle(randomized_tests)
        tmp._tests = (t for t in randomized_tests)
        return tmp
