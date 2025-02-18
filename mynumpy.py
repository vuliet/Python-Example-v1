import numpy as np

# Tạo mảng NumPy
print('2. Tạo mảng Numpy')
arr = np.array([1, 2, 3, 4, 5])

# Mảng 2 chiều (Ma trận)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)  # [1 2 3 4 5]
print(matrix)

# Tạo mảng số ngẫu nhiên
print('2. Tạo mảng số ngẫu nhiên')
random_arr = np.random.randint(0, 100, (3, 3))
print(random_arr)

# Tính toán với NumPy
arr = np.array([10, 20, 30])
print(arr + 5)  # [15 25 35]
print(arr * 2)  # [20 40 60]
