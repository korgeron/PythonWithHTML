"""
    Define a function to test
"""


def func(x):
    """
        This code will fail the test below. To pass must be x + 2
    """
    return x + 1


"""
    Test the function above
"""


def test_func():
    assert func(3) == 5
