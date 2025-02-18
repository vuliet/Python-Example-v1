# Machine Learning với Scikit-learn
# Scikit-learn giúp xây dựng mô hình Machine Learning cơ bản.
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dữ liệu mẫu (diện tích và giá nhà)
data = {
    "Diện tích": [50, 60, 80, 100, 120],
    "Giá nhà": [150, 180, 220, 300, 350]
}
df = pd.DataFrame(data)

# Chia dữ liệu thành biến độc lập (X) và phụ thuộc (y)
X = df[["Diện tích"]]
y = df["Giá nhà"]

# Chia thành tập train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán giá nhà cho diện tích 90m²
predicted_price = model.predict([[90]])
print(f"Giá nhà dự đoán: {predicted_price[0]} triệu")
