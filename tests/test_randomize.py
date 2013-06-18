"""
Tests that plugins can override loadTestsFromTestCase

The original source of the code is:

http://code.google.com/p/python-nose/issues/detail?id=255

and the original author is: Charles McCreary
"""
import os
import unittest
from nose.plugins import PluginTester
from randomize import Randomize

support = os.path.join(os.path.dirname(__file__), 'support')


class TestRandomizePlugin(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=2530711073']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures.py')

    def runTest(self):
        expect = [
            'test_C (fixtures.Tests) ... ok',
            'test_B (fixtures.Tests) ... ok',
            'test_A (fixtures.Tests) ... ok',
            'test_D (fixtures.Tests) ... ok']
        print str(self.output)
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


class TestRandomizePluginMultipleTestClasses(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=1234112']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_two_classes.py')

    def runTest(self):
        expect = [
            'test_C (fixtures.Tests) ... ok',
            'test_B (fixtures.Tests) ... ok',
            'test_A (fixtures.Tests) ... ok',
            'test_D (fixtures.Tests) ... ok']
        print str(self.output)
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


class TestRandomizePluginLooseTestFunctions(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=1234112']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_loose.py')

    def runTest(self):
        expect = [
            'test_C (fixtures.Tests) ... ok',
            'test_B (fixtures.Tests) ... ok',
            'test_A (fixtures.Tests) ... ok',
            'test_D (fixtures.Tests) ... ok']
        print str(self.output)
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


if __name__ == '__main__':
    unittest.main()
