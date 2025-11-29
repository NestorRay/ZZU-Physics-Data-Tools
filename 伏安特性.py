from matplotlib import pyplot as plt
import numpy as np

# 这两行代码使得 pyplot 画出的图形中可以显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.array([0.54,0.55,0.56,0.57,0.59,0.60,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.70,0.71,0.72,0.73,0.74,0.75 ])
y = np.array([0.30,0.30,0.40,0.50,0.70,1.00,1.20,1.50,1.70,2.20,3.10,3.60,4.40,6.00,7.60,9.10,10.60,12.90,15.60,20.30,24.90])
y_log = np.log(y)

k,b = np.polyfit(x,y_log,deg = 1)

y_fit = k * x + b



print(k,b)
# 生成图形
plt.plot(x, y_log, 'ko-', linewidth=2) # 颜色绿色，点形圆形，线性虚线，设置图例显示内容，线条宽度为2
plt.plot(x, y_fit, 'r--', linewidth=2, label=f'回归线：ln(I) = {k:.2f}U + {b:.2f}') 
plt.ylabel('I(mA)') # 横坐标轴的标题a
plt.xlabel('U(V)') # 纵坐标轴的标题
plt.xticks([0.5, 0.8]) # 设置横坐标轴的刻度为 0 到 10 的数组
plt.ylim([-2,4]) # 设置纵坐标轴范围为 -2 到 2
plt.legend() # 显示图例, 图例中内容由 label 定义
# plt.grid() # 显示网格
plt.title('普通二极管正向') # 图形的标题

# 显示图形
plt.show() 
