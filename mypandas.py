import pandas as pd

# Tạo DataFrame từ dictionary
data = {
    "Tên": ["Alice", "Bob", "Charlie"],
    "Tuổi": [25, 30, 35],
    "Lương": [5000, 7000, 9000]
}
df = pd.DataFrame(data)

# Hiển thị dữ liệu
print(df)

# Đọc dữ liệu từ file CSV
df = pd.read_csv("data.csv")  # Đọc file CSV
print(df.head())  # Xem 5 dòng đầu tiên

# Xử lý dữ liệu trong Pandas
# Lọc dữ liệu (Những người có lương trên 6000)
filtered_df = df[df["Lương"] > 6000]

# Thêm cột mới
df["Thưởng"] = df["Lương"] * 0.1

# Xóa cột
df.drop(columns=["Thưởng"], inplace=True)

print(df)
