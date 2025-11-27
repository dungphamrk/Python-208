# Sản phẩm: Áo, Quần, Giày, Túi, Mũ, Tất
# Doanh số (triệu): 150, 120, 200, 90, 65, 80
# Vẽ cột màu xanh lá, viền đen
# In giá trị doanh số lên đầu mỗi cột (chữ trắng, đậm)
# Tiêu đề: “Doanh số bán hàng tháng 10/2025”
import matplotlib.pyplot as plt
import numpy as np
products = ['Áo', 'Quần', 'Giày', 'Túi', 'Mũ', 'Tất']
sales = [150, 120, 200, 90, 65, 80]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(products, sales, color='green', edgecolor='black')
ax.set_title("Doanh số bán hàng tháng 10/2025", fontsize=16)
ax.set_xlabel("Sản phẩm", fontsize=14)
ax.set_ylabel("Doanh số (triệu)", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.6)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height}', ha='center', va='bottom',
            color='white', fontweight='bold')
plt.show()