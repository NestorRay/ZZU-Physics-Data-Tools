import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
from scipy import stats

# # 设置中文字体和样式
# plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']
# plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# 解决方案1：设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成模拟数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
time_series = np.cumsum(np.random.randn(100)) + 20
categories = ['生物', '化学', '物理', '工程', '医学']
values1 = np.random.normal(100, 20, 1000)
values2 = np.random.normal(120, 25, 1000)

# 创建复杂的多子图布局
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(3, 4, figure=fig)

# 子图1: 时间序列与趋势线
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(x, time_series, 'b-', alpha=0.7, linewidth=2, label='实验数据')
# 添加趋势线
z = np.polyfit(range(len(time_series)), time_series, 3)
p = np.poly1d(z)
ax1.plot(x, p(range(len(time_series))), 'r--', linewidth=2, label='趋势线')
ax1.fill_between(x, time_series, alpha=0.3)
ax1.set_title('A) 时间序列分析与趋势预测', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 子图2: 分布直方图与密度曲线
ax2 = fig.add_subplot(gs[0, 2:])
sns.histplot(values1, kde=True, color='skyblue', ax=ax2, label='对照组', alpha=0.7)
sns.histplot(values2, kde=True, color='salmon', ax=ax2, label='实验组', alpha=0.7)
ax2.set_title('B) 实验组与对照组分布比较', fontsize=14, fontweight='bold')
ax2.legend()

# 子图3: 箱线图
ax3 = fig.add_subplot(gs[1, :2])
data_box = [np.random.normal(i, 1, 50) for i in range(5)]
bp = ax3.boxplot(data_box, labels=categories, patch_artist=True)
# 设置箱线图颜色
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'plum']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
ax3.set_title('C) 多学科数据分布比较', fontsize=14, fontweight='bold')

# 子图4: 热力图
ax4 = fig.add_subplot(gs[1, 2:])
correlation_matrix = np.random.rand(8, 8)
np.fill_diagonal(correlation_matrix, 1)
im = ax4.imshow(correlation_matrix, cmap='RdYlBu_r', aspect='auto')
ax4.set_xticks(range(8))
ax4.set_yticks(range(8))
ax4.set_xticklabels([f'因子{i+1}' for i in range(8)])
ax4.set_yticklabels([f'因子{i+1}' for i in range(8)])
plt.colorbar(im, ax=ax4)
ax4.set_title('D) 多因子相关性热图', fontsize=14, fontweight='bold')

# 子图5: 3D曲面图
from mpl_toolkits.mplot3d import Axes3D
ax5 = fig.add_subplot(gs[2, :], projection='3d')
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax5.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
ax5.set_title('E) 3D曲面可视化: 波动函数模型', fontsize=14, fontweight='bold')
fig.colorbar(surf, ax=ax5, shrink=0.5)

plt.tight_layout()
plt.show()