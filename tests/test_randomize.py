"""
Tests that plugins can override loadTestsFromTestCase
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


if __name__ == '__main__':
    unittest.main()
