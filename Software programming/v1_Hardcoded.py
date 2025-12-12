import math

a = 2
b = -7
c = 3

discriminant = b*b - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1:.2f} and {root2:.2f}")

elif discriminant == 0:
    root1 = -b / (2 * a)
    print(f"Roots: {root1:.2f} and {root1:.2f} (equal roots)")

else:
    print("No real roots")
