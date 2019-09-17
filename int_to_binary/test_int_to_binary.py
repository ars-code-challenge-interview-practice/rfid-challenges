import pytest
from int_to_binary import int_to_binary

def test_exists():
    assert int_to_binary

def test_single_digits_no_space():

    assert int_to_binary(1) == '1'
    assert int_to_binary(2) == '10'
    assert int_to_binary(3) == '11'
    assert int_to_binary(4) == '100'
    assert int_to_binary(5) == '101'
    assert int_to_binary(6) == '110'
    assert int_to_binary(7) == '111'
    assert int_to_binary(8) == '1000'
    assert int_to_binary(9) == '1001'









    