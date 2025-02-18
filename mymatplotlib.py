import matplotlib.pyplot as plt

# Dữ liệu mẫu
names = ["Alice", "Bob", "Charlie"]
salaries = [5000, 7000, 9000]

# Vẽ biểu đồ
plt.bar(names, salaries, color="skyblue")
plt.xlabel("Nhân viên")
plt.ylabel("Lương")
plt.title("Lương nhân viên")
plt.show()
