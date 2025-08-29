import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.lines import Line2D

# Đọc dữ liệu từ file
x = []
y = []

with open(r'D:\Mobile_Robot\YOLOv9_Object_Tracking\28_9_2024\exp20\m.txt') as file:
    for line in file:
        point = line.strip().split()
        x.append(float(point[0]))
        y.append(float(point[1]))

# Tạo đồ thị
fig, ax = plt.subplots(figsize=(8, 6))  # Điều chỉnh kích thước của đồ thị nếu cần

# Vẽ điểm dữ liệu
ax.scatter(x, y, color='red', s=0.3)

# Đặt tên trục với khoảng cách điều chỉnh
ax.set_xlabel('x (m)', labelpad=-30)  # Điều chỉnh khoảng cách của nhãn trục x
ax.set_ylabel('y (m)', labelpad=-50, rotation=0)  # Điều chỉnh khoảng cách của nhãn trục y

# Đặt tiêu đề cho đồ thị
ax.set_title('Quỹ đạo di chuyển của robot trên hệ toạ độ thực', pad=20)  # Điều chỉnh khoảng cách của tiêu đề so với đồ thị

# Di chuyển trục tọa độ vào giữa
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Ẩn các trục không cần thiết
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Đặt vị trí các tick
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Đặt giới hạn cho các trục
ax.set_xlim(-1.65, 1.65)
ax.set_ylim(-1.20, 1.20)

# Thiết lập lưới với khoảng cách 15 đơn vị
ax.xaxis.set_major_locator(MultipleLocator(15))
ax.yaxis.set_major_locator(MultipleLocator(15))

# Đặt vị trí các tick
ax.set_xticks([-1.65, -1.35, -1.05, -0.75, -0.45, -0.15, 0, 0.15, 0.45, 0.75, 1.05, 1.35, 1.65])
ax.set_yticks([-1.20, -0.90, -0.60, -0.30, 0, 0.30, 0.60, 0.90, 1.20])

# Hiển thị lưới tọa độ
ax.grid(which='both', linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')

xticks = ax.get_xticks().tolist()
yticks = ax.get_yticks().tolist()
xticks.remove(0)
yticks.remove(0)
ax.set_xticks(xticks)
ax.set_yticks(yticks)

# Vẽ các đường biên
line1 = Line2D([ax.get_xlim()[0], ax.get_xlim()[1]], [ax.get_ylim()[0], ax.get_ylim()[0]], color='black', alpha=0.2)
line2 = Line2D([ax.get_xlim()[0], ax.get_xlim()[1]], [ax.get_ylim()[1], ax.get_ylim()[1]], color='black', alpha=0.2)
line3 = Line2D([ax.get_xlim()[0], ax.get_xlim()[0]], [ax.get_ylim()[0], ax.get_ylim()[1]], color='black', alpha=0.2)
line4 = Line2D([ax.get_xlim()[1], ax.get_xlim()[1]], [ax.get_ylim()[0], ax.get_ylim()[1]], color='black', alpha=0.2)

ax.add_line(line1)
ax.add_line(line2)
ax.add_line(line3)
ax.add_line(line4)

# Điều chỉnh vị trí của nhãn trục X và Y ra ngoài khung hình
ax.xaxis.label.set_position((1, 0.1))  # (hệ số điều chỉnh ngang, hệ số điều chỉnh dọc)
ax.yaxis.label.set_position((0.1, 1))  # (hệ số điều chỉnh ngang, hệ số điều chỉnh dọc)

# Hiển thị đồ thị
plt.tight_layout(pad=1.0)  # Tự động điều chỉnh các yếu tố để phù hợp với khung hình

# Lưu đồ thị để kiểm tra kích thước
plt.savefig('plot_28_9_2024_11h22.png', bbox_inches='tight', pad_inches=0.1, dpi=1500)
plt.show()
