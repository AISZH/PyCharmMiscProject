import numpy as np
import matplotlib.pyplot as plt

# 1. 定义函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# 2. 生成 x 轴数据（覆盖正负区间，让图像更完整）
x = np.linspace(-10, 10, 1000)  # 从-10到10，取1000个点
y_sigmoid = sigmoid(x)
y_relu = relu(x)

# 3. 创建画布，绘制两个子图
plt.figure(figsize=(12, 5))

# 子图1：Sigmoid 函数
plt.subplot(1, 2, 1)
plt.plot(x, y_sigmoid, color='#2E86AB', linewidth=2.5, label='Sigmoid')
plt.title('Sigmoid 函数', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('σ(x)', fontsize=12)
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.6)  # 中间线
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.6)    # 对称轴
plt.grid(alpha=0.3)
plt.legend()

# 子图2：ReLU 函数
plt.subplot(1, 2, 2)
plt.plot(x, y_relu, color='#A23B72', linewidth=2.5, label='ReLU')
plt.title('ReLU 函数', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('ReLU(x)', fontsize=12)
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.6)    # 分割线
plt.grid(alpha=0.3)
plt.legend()

# 4. 调整布局并显示图像
plt.tight_layout()
plt.show()