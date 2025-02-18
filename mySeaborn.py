import seaborn as sns

# Dữ liệu ngẫu nhiên
data = np.random.normal(50, 15, 1000)

# Vẽ biểu đồ phân bố
sns.histplot(data, kde=True)
plt.show()
