"""
Tests that plugins can override loadTestsFromTestCase

The original source of the code is:

http://code.google.com/p/python-nose/issues/detail?id=255

and the original author is: Charles McCreary
"""
import os
import unittest
import sys
from nose.plugins import PluginTester
from randomize import Randomize

support = os.path.join(os.path.dirname(__file__), 'support')


class TestRandomizePlugin(PluginTester, unittest.TestCase):
    activate = '--randomize'
    if (sys.version_info > (3, 0)):
        args = ['-v', '--seed=2531']
    else:
        args = ['-v', '--seed=2530711073']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures.py')

    def runTest(self):
        expect = [
            'test_C (fixtures.Tests) ... ok',
            'test_B (fixtures.Tests) ... ok',
            'test_A (fixtures.Tests) ... ok',
            'test_D (fixtures.Tests) ... ok']
        print(str(self.output))
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


@unittest.skip("Skipping test until the classes can be shuffled")
class TestRandomizePluginMultipleTestClasses(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=1234112']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_two_classes.py')

    def runTest(self):
        expect = [
            'test_C (fixtures_two_classes.Tests_C_set) ... ok',
            'test_B (fixtures_two_classes.Tests_B_set) ... ok',
            'test_A (fixtures_two_classes.Tests_A_set) ... ok',
            'test_D (fixtures_two_classes.Tests_D_set) ... ok']
        print(str(self.output))
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


class TestRandomizePluginLooseTestFunctions(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=54642']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_loose.py')

    def runTest(self):
        expect = [
            'fixtures_loose.test_loose_A ... ok',
            'fixtures_loose.test_loose_B ... ok',
            'fixtures_loose.test_loose_C ... ok',
            'fixtures_loose.test_loose_D ... ok']
        print(str(self.output))
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


class TestRandomizePluginNoTestFunctions(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=521115']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_not_tests.py')

    def runTest(self):
        expect = []
        print(str(self.output))
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


class TestRandomizePluginNoTUnitTestBased(PluginTester, unittest.TestCase):
    activate = '--randomize'
    if (sys.version_info > (3, 0)):
        args = ['-v', '--seed=12499']
    else:
        args = ['-v', '--seed=521115']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'fixtures_not_unittest.py')

    def runTest(self):
        expect = ["fixtures_not_unittest.Test_something_not_unittest.test_A_3 ... ok",
        "fixtures_not_unittest.Test_something_not_unittest.test_A_1 ... ok",
        "fixtures_not_unittest.Test_something_not_unittest.test_A_4 ... ok",
        "fixtures_not_unittest.Test_something_not_unittest.test_A_2 ... ok"]
        print(str(self.output))
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))

if __name__ == '__main__':
    unittest.main()
