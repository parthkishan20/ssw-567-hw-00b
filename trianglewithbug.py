# triangle_buggy.py
def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"

    # BUG: should be <= (not <)
    if a + b < c or a + c < b or b + c < a:
        return "Invalid"

    sides = sorted([a, b, c])
    x, y, z = sides
    is_right = (x * x + y * y == z * z)

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Right Isosceles" if is_right else "Isosceles"

    return "Right Scalene" if is_right else "Scalene"
