import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,50)
y=x**2
fix, ax = plt.subplots(figsize=(8,4))
ax.set_title("Biểu đồ mới ")
ax.plot(x,y,color='green',linewidth=2,linestyle='--',marker='o',markerfacecolor='red',markersize=6)
ax.set_xlabel("Trục X",fontsize=14)
ax.set_ylabel("Trục Y",fontsize=14)
plt.show()