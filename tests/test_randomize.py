"""
Tests that plugins can override loadTestsFromTestCase
"""
import os
import unittest
from nose import loader
from nose.plugins import PluginTester
from nose.plugins.randomize import Randomize
from nose.plugins.base import Plugin

support = os.path.join(os.path.dirname(__file__), 'support')


class TestRandomizePlugin(PluginTester, unittest.TestCase):
    activate = '--randomize'
    args = ['-v', '--seed=2530711073']
    plugins = [Randomize()]
    suitepath = os.path.join(support, 'randomize')

    def runTest(self):
        expect = [
            'test_C (tests.Tests) ... ok',
            'test_B (tests.Tests) ... ok',
            'test_A (tests.Tests) ... ok',
            'test_D (tests.Tests) ... ok']
        print str(self.output)
        for line in self.output:
            if expect:
                self.assertEqual(line.strip(), expect.pop(0))


if __name__ == '__main__':
    unittest.main()
