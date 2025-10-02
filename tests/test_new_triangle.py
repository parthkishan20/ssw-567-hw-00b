# tests/test_new_triangle.py

from math import sqrt
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from triangle import classify_triangle


def test_right_isosceles_float():
    """
    NEW: cover the 'Right Isosceles' branch using floats (1, 1, sqrt(2)).
    """
    assert classify_triangle(1.0, 1.0, sqrt(2)) == "Right Isosceles"


def test_isosceles_with_floats():
    """
    NEW: ensure floats work for a non-right isosceles.
    """
    assert classify_triangle(2.0, 2.0, 3.0) == "Isosceles"


def test_large_scalene_valid():
    """
    NEW: larger values still classified correctly.
    """
    assert classify_triangle(50, 60, 70) == "Scalene"


def test_obvious_inequality_violation():
    """
    NEW: clearly invalid by triangle inequality.
    """
    assert classify_triangle(100, 1, 1) == "Invalid"
