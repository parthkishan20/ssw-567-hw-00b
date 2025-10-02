"""
Test module demonstrating bugs in the trianglewithbug module.

This module contains tests that are expected to fail due to known bugs
in the triangle classification implementation.
"""
# tests/test_bug_demo.py
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from trianglewithbug import classify_triangle as classify_triangle_buggy


@pytest.mark.xfail(
    reason="Bug triangle code wrongly treats degenerate triangles as valid",
    strict=True
)
def test_buggy_degenerate_triangle_should_be_invalid():
    """
    Test that demonstrates buggy triangle classification for degenerate triangles.
    
    This test is expected to fail because the buggy implementation
    incorrectly accepts degenerate triangles as valid.
    """
    # This is NOT a valid triangle (1 + 2 == 3), but buggy code allows it.
    assert classify_triangle_buggy(1, 2, 3) == "Invalid"
