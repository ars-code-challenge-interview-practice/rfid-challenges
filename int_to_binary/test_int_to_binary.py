import pytest
from int_to_binary import int_to_binary

def test_exists():
    assert int_to_binary

def test_single_digits_no_space():
    one = 1
    two = 2
    three = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

    assert self.int_to_binary(1) == '1'
    assert self.int_to_binary(2) == '10'
    assert self.int_to_binary(3) == '11'
    assert self.int_to_binary(4) == '100'
    assert self.int_to_binary(5) == '101'
    assert self.int_to_binary(6) == '110'
    assert self.int_to_binary(7) == '111'
    assert self.int_to_binary(8) == '1000'
    assert self.int_to_binary(9) == '1001'








    