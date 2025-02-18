# TensorFlow giúp xây dựng mô hình học sâu (Deep Learning).
# Ví dụ: Mạng nơ-ron nhân tạo cơ bản
import tensorflow as tf
from tensorflow import keras

# Tạo mô hình mạng nơ-ron đơn giản
model = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=(10,)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1)  # Lớp đầu ra
])

# Compile mô hình
model.compile(optimizer="adam", loss="mse")

# Hiển thị kiến trúc mô hình
model.summary()
