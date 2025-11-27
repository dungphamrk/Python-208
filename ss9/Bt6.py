import matplotlib.pyplot as plt
import numpy as np
years = np.arange(2015, 2025)
population = np.array([92, 93, 94, 95, 96, 97, 98, 99, 100, 101])
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("Tăng trưởng dân số Việt Nam 2015–2024", fontsize=16)
ax.plot(years, population, color='blue', linestyle='-', marker='o', label='Dân số (triệu người)')
ax.set_xlabel("Năm", fontsize=14)
ax.set_ylabel("Dân số (triệu người)", fontsize=14)
ax.grid(linestyle='--', alpha=0.6)
ax.legend(loc="upper left", fontsize=12)
plt.show()