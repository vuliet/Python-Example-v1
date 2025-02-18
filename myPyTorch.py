# PyTorch là một thư viện mạnh mẽ để xử lý Deep Learning.
# Ví dụ: Tạo mô hình nơ-ron nhân tạo với PyTorch
import torch
import torch.nn as nn

# Định nghĩa mô hình
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 64)
        self.fc2 = nn.Linear(64, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Khởi tạo mô hình
model = SimpleNN()
print(model)
