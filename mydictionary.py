# Tạo dictionary
# Dictionary lưu dữ liệu theo cặp key: value.
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Truy cập giá trị
print(student["name"])  # Alice

# Thêm phần tử
student["city"] = "New York"

# Duyệt dictionary
for key, value in student.items():
    print(key, ":", value)
