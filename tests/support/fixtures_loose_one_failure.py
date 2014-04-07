"""
'loose' test functions, with A failing
"""
from nose.tools import assert_equals


class TestBailEarlyOnError():
    def test_loose_A(self):
        assert_equals(1, 2)

    def test_loose_B(self):
        pass

    def test_loose_C(self):
        pass

    def test_loose_D(self):
        pass
