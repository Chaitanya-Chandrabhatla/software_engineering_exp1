import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 0.8
b = -2.0
c = 15.0

# Time values
time = np.linspace(0, 10, 100)

# Temperature calculation
temp = (a * time**2) + (b * time) + c

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, temp, linewidth=2, label="Final Output")
plt.title("Waterfall Model")
plt.xlabel("Time (hours)")
plt.ylabel("Temp (°C)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

print("Graph generated")
plt.show()
