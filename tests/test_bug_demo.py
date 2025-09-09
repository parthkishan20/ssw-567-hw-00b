# tests/test_bug_demo.py
import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from trianglewithbug import classify_triangle as classify_triangle_buggy

@pytest.mark.xfail(reason="Bug triangle code wrongly treats degenerate triangles as valid", strict=True)
def test_buggy_degenerate_triangle_should_be_invalid():
    # This is NOT a valid triangle (1 + 2 == 3), but buggy code allows it.
    assert classify_triangle_buggy(1, 2, 3) == "Invalid"
