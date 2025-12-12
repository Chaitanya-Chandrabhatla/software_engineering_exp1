import math

# Try to open the file
try:
    with open("Software programming/input_multiple_Sets.txt", "r") as fp:
        lines = fp.readlines()
except FileNotFoundError:
    print("File not found")
    exit()

# Process each line
for line in lines:
    # Skip empty lines
    if not line.strip():
        continue

    try:
        a, b, c = map(float, line.split())
    except:
        print("Invalid line:", line)
        continue

    print(f"Equation: {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
