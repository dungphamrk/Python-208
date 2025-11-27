import matplotlib.pyplot as plt
import numpy as np
months= list(range(1,13))
rainfall=[78,60,55,48,40,35,30,32,45,60,70,80]
temperature=[30,32,35,38,40,42,45,44,40,35,33,31]
fig, ax = plt.subplots(figsize=(10,5))
ax.set_title("Biểu đồ lượng mưa và nhiệt độ theo tháng", fontsize=16)
ax.bar(months, rainfall, color='blue', alpha=0.6, label='Lượng mưa (mm)')
ax.set_xlabel("Tháng", fontsize=14) 
ax.set_ylabel("Lượng mưa (mm)", fontsize=14)
ax2 = ax.twinx()
ax2.plot(months, temperature, color='red', marker='o', label='Nhiệt độ (°C)')
ax2.set_ylabel("Nhiệt độ (°C)", fontsize=14)
fig.legend(loc="upper right", bbox_to_anchor=(0.9,0.9), bbox_transform=ax.transAxes)
plt.show()