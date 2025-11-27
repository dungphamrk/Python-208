
import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(-5, 5, 100)
y = x**3
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("Đồ thị hàm bậc ba y = x³", fontsize=16)
ax.plot(x, y, color='red', linewidth=3)
ax.set_xlabel("Giá trị x", fontsize=14)
ax.set_ylabel("Giá trị y", fontsize=14)
ax.grid(linestyle='--', alpha=0.6)
plt.show()
