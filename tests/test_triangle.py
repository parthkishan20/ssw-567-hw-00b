"""
Test module for triangle classification functionality.

This module contains comprehensive tests for the classify_triangle function,
covering all triangle types including equilateral, isosceles, scalene,
right triangles, and invalid triangles.
"""
# tests/test_triangle.py
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from triangle import classify_triangle

# --- Equilateral ---
def test_equilateral():
    """Test classification of equilateral triangles."""
    assert classify_triangle(2, 2, 2) == "Equilateral"

# --- Isosceles (not right) ---
@pytest.mark.parametrize("a,b,c", [
    (5, 5, 8),
    (8, 5, 5),
    (5, 8, 5),
])
def test_isosceles(a, b, c):
    """Test classification of isosceles triangles."""
    assert classify_triangle(a, b, c) == "Isosceles"

# --- Scalene (not right) ---
@pytest.mark.parametrize("a,b,c", [
    (4, 5, 6),
    (7, 8, 9),
])
def test_scalene(a, b, c):
    """Test classification of scalene triangles."""
    assert classify_triangle(a, b, c) == "Scalene"

# --- Right (3-4-5 family) should be Right Scalene ---
@pytest.mark.parametrize("a,b,c", [
    (3, 4, 5),
    (4, 5, 3),
    (5, 3, 4),
    (6, 8, 10),   # scaled 3-4-5
])
def test_right_scalene(a, b, c):
    """Test classification of right scalene triangles."""
    assert classify_triangle(a, b, c) == "Right Scalene"

# --- Invalid: non-positive sides ---
@pytest.mark.parametrize("a,b,c", [
    (0, 1, 1),
    (-1, 2, 2),
    (2, -1, 2),
    (2, 2, -1),
])
def test_invalid_non_positive(a, b, c):
    """Test that triangles with non-positive sides are invalid."""
    assert classify_triangle(a, b, c) == "Invalid"

# --- Invalid: triangle inequality violated or degenerate ---
@pytest.mark.parametrize("a,b,c", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 1, 9),   # 1 + 9 == 10 (degenerate, still invalid)
])
def test_invalid_triangle_inequality(a, b, c):
    """Test that triangles violating triangle inequality are invalid."""
    assert classify_triangle(a, b, c) == "Invalid"
