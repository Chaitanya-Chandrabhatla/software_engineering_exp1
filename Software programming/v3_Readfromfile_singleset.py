import math

# Try opening the file
try:
    with open("Software programming/input_Single_Set.txt", "r") as fp:

        a, b, c = map(float, fp.read().split())
except FileNotFoundError:
    print("File not found")
    exit()

# Calculate discriminant
discriminant = b * b - 4 * a * c

# Check cases
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1:.2f} and {root2:.2f}")

elif discriminant == 0:
    root1 = -b / (2 * a)
    print(f"Roots: {root1:.2f} and {root1:.2f} (equal roots)")

else:
    print("No real roots")
