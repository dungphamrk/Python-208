
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = 2 * x + 1
y2 = -x + 10
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("Giao điểm của hai đường thẳng", fontsize=16)
ax.plot(x, y1, color='blue', label='Đường 1')
ax.plot(x, y2, color='orange', label='Đường 2')
ax.set_xlabel("Giá trị x", fontsize=14)
ax.set_ylabel("Giá trị y", fontsize=14)
ax.grid(linestyle='--', alpha=0.6)
ax.legend(loc="upper left", fontsize=12)
plt.show()
