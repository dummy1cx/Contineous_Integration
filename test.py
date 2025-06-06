import pytest

# Functions to test
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

# ✅ Corrected test function names (typos fixed)
def test_square():
    assert square(2) == 4, "Test failed: Square of 2 should be 4"
    assert square(3) == 9, "Test failed: Square of 3 should be 9"

def test_cube():
    assert cube(3) == 27, "Test failed: Cube of 3 should be 27"
    assert cube(2) == 8, "Test failed: Cube of 2 should be 8"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed: Fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test failed: Fifth power of 3 should be 243"

# ✅ Good practice: Testing invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
