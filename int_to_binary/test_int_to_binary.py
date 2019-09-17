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


def test_two_digits():
    assert int_to_binary(10) == '1010'
    assert int_to_binary(21) == '10101'
    assert int_to_binary(32) == '100000'
    assert int_to_binary(43) == '101011'
    assert int_to_binary(54) == '110110'

def test_zero():
    assert int_to_binary(0) == '0'

def test_negatives():
    assert int_to_binary(-1) == '-1'
    assert int_to_binary(-500) == '-111110100'
    assert int_to_binary(-25) == '-11001'
    assert int_to_binary(-1000) == '1111101000'



    