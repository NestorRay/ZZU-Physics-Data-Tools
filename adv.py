import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
import numpy as np

sns.set_style("whitegrid")

# 解决方案1：设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 创建模拟实验数据
np.random.seed(123)
n_samples = 300

# 生成聚类数据
X, y = make_blobs(n_samples=n_samples, centers=4, n_features=2, 
                  random_state=42, cluster_std=1.5)

# 创建DataFrame
df = pd.DataFrame(X, columns=['特征1', '特征2'])
df['类别'] = y
df['时间'] = np.random.randint(1, 100, n_samples)
df['数值'] = np.random.exponential(2, n_samples)

# 创建多面板统计图
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 散点图与聚类
scatter = axes[0,0].scatter(df['特征1'], df['特征2'], c=df['类别'], 
                           cmap='Set2', s=50, alpha=0.7)
axes[0,0].set_xlabel('特征 1')
axes[0,0].set_ylabel('特征 2')
axes[0,0].set_title('A) 数据聚类分析', fontweight='bold')
plt.colorbar(scatter, ax=axes[0,0])

# 小提琴图
sns.violinplot(data=df, x='类别', y='数值', ax=axes[0,1], palette='Set2')
axes[0,1].set_title('B) 各类别数据分布（小提琴图）', fontweight='bold')

# 累积分布函数
for category in df['类别'].unique():
    data = df[df['类别'] == category]['数值']
    sorted_data = np.sort(data)
    y_vals = np.arange(len(sorted_data)) / float(len(sorted_data))
    axes[1,0].plot(sorted_data, y_vals, label=f'类别 {category}', linewidth=2)
axes[1,0].set_xlabel('数值')
axes[1,0].set_ylabel('累积概率')
axes[1,0].set_title('C) 累积分布函数比较', fontweight='bold')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

# 2D密度图
sns.kdeplot(data=df, x='特征1', y='特征2', fill=True, cmap='Blues', ax=axes[1,1])
axes[1,1].set_xlabel('特征 1')
axes[1,1].set_ylabel('特征 2')
axes[1,1].set_title('D) 二维概率密度分布', fontweight='bold')

plt.tight_layout()
plt.show()