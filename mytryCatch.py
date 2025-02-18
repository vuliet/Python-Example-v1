try:
    x = 10 / 0  # Lỗi chia cho 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
finally:
    print("Luôn luôn chạy đoạn này.")
