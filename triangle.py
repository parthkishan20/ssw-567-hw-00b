def classify_triangle(a, b, c):

    #checking if input is valid triangle or not
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    
    #sorting the sides to easily check for right triangle
    sides = sorted([a, b, c])
    x, y, z = sides  # x <= y <= z

    # Checking for right triangle using Pythagorean theorem
    is_right_triangle = (x * x + y * y == z * z)

    # Equilateral
    if a == b == c:
        return "Equilateral"

    # Isosceles
    if a == b or b == c or a == c:
        if is_right_triangle:
            return "Right Isosceles"
        return "Isosceles"

    # Scalene
    if is_right_triangle:
        return "Right Scalene"
    return "Scalene"

if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))   # Right Scalene
    print(classify_triangle(2, 2, 2))   # Equilateral
    print(classify_triangle(5, 5, 8))   # Isosceles
    print(classify_triangle(1, 2, 3))   # Invalid