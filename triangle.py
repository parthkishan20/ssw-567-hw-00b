"""
Module for classifying triangles based on their side lengths.

This module provides functionality to classify triangles as equilateral,
isosceles, scalene, or invalid based on the lengths of their sides.
"""
from typing import Union, Sequence
import math

Number = Union[int, float]


def classify_triangle(a: Number, b: Number, c: Number) -> str:
    """
    Classify a triangle based on the lengths of its sides.
    
    Args:
        a (Number): Length of first side
        b (Number): Length of second side  
        c (Number): Length of third side
        
    Returns:
        str: Triangle classification - one of:
             - "Invalid": Not a valid triangle
             - "Equilateral": All sides equal
             - "Isosceles": Two sides equal
             - "Scalene": All sides different
             - "Right Isosceles": Right triangle with two equal sides
             - "Right Scalene": Right triangle with all different sides
    """


    # 1) validity checks
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    # 2) sort sides so z is the longest; helps with right-triangle check
    sides: Sequence[Number] = sorted([a, b, c])
    x, y, z = sides  # x <= y <= z

    # 3) right-triangle check (Pythagoras)
    is_right_triangle = math.isclose(x * x + y * y, z * z)

    # 4) type checks
    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Right Isosceles" if is_right_triangle else "Isosceles"

    return "Right Scalene" if is_right_triangle else "Scalene"


if __name__ == "__main__":  # pragma: no cover
    # Quick demo run (excluded from coverage report)
    print(classify_triangle(3, 4, 5))   # Right Scalene
    print(classify_triangle(2, 2, 2))   # Equilateral
    print(classify_triangle(5, 5, 8))   # Isosceles
    print(classify_triangle(1, 2, 3))   # Invalid
