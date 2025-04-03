import pytest

# A simple test that will pass
def test_addition():
    assert 2 + 2 == 4

# A test that will fail
def test_subtraction():
    assert 5 - 2 == 4  # This will fail because 5 - 2 is 3, not 4

# A test that will raise an exception (to test error handling)
def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# A simple test for string comparison
def test_string():
    assert "hello" == "world"  # This will fail because the strings don't match
