
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 20)
y = 2 * x + 3
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("Đường thẳng y = 2x + 3", fontsize=16)
ax.plot(x, y, color='blue', linewidth=3)
ax.set_xlabel("Giá trị x", fontsize=14)
ax.set_ylabel("Giá trị y", fontsize=14)
ax.grid(linestyle='--', alpha=0.6)
plt.show()