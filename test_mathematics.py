# test_mathematics.py
from mathematics import multiply, divide, round_up, hypotenuse


def test_multiplication():
    assert multiply(4, 5) == 20


def test_division():
    assert divide(4, 5) == 0.8


def test_round_up():
    assert round_up(2.4) == 3


# Add this test to `test_mathematics.py`
def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

            |\
          L | \
          g |   \
         (A)|    \
            ------
            Leg(B)

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(3, 4) == 5

