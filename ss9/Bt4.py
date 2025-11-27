
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("So sánh sin(x) và cos(x)", fontsize=16)
ax.plot(x, y1, color='blue', linestyle='-', label='sin(x)')
ax.plot(x, y2, color='red', linestyle='--', label='cos(x)')
ax.set_xlabel("Giá trị x (radians)", fontsize=14)   
ax.set_ylabel("Giá trị y", fontsize=14)
ax.legend(loc="upper right", fontsize=12)
plt.show()
