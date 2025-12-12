import math

# Taking input
a, b, c = map(float, input("Enter coefficients a b c: ").split())

# Calculating discriminant
discriminant = b*b - 4*a*c

# Checking conditions
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1:.2f} and {root2:.2f}")

elif discriminant == 0:
    root1 = -b / (2 * a)
    print(f"Roots: {root1:.2f} and {root1:.2f} (equal roots)")

else:
    print("No real roots")
