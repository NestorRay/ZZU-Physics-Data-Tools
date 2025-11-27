import numpy as np
from scipy.optimize import approx_fprime

data = np.zeros((4,6,2))

data[0] = ([[144,18],
            [136,44],
            [129,15],
            [150,10],
            [157,30],
            [151,51]])

data[1] = ([[324,16],
            [316,42],
            [309,10],
            [330,16],
            [337,30],
            [331,50]])

data[2] = ([[195,36],
            [188,00],
            [180,35],
            [202,6],
            [208,45],
            [203,11]])

data[3] = ([[375,34],
            [368,0],
            [360,30],
            [382,4],
            [388,45],
            [383,6]])

# print(data[...,0])
deg = data[:,:,0]+data[...,1]/60

dt1 = deg[2,...]-deg[0,...]
dt2 = deg[3,...]-deg[1,...]

resu = 0.5*(dt1+dt2)
# print(dt1,'\n',dt2)
print(resu)
print("-------------------------------")
print("最小偏向角: ",np.mean(resu))
print("A类不确定度: ",np.sqrt(np.var(resu,ddof=1)))
# print(deg)
# print(data)


#以下计算折射率
A = 60
delta = np.mean(resu)
n = np.sin(np.deg2rad((delta+A)/2))/np.sin(np.deg2rad(A/2))
print("折射率: ",f"{n }")

# 以下实现数值偏导
def binary_func(vars): #先A后delta
    x,y = vars #A = x delta = y 
    return np.sin(np.deg2rad((y+x)/2))/np.sin(np.deg2rad(x/2))

y_target = np.mean(resu)
x_fixed = 60
vars_y = np.array([x_fixed, y_target], dtype=np.float64)
epsilon = 1e-6 
partial_y = approx_fprime(vars_y, binary_func, epsilon)[1]
print(f"在(x={x_fixed}, y={y_target})处，对y的偏导：{partial_y:.6f}")
error = (partial_y/n)*100
print(f"相对误差为：{error}%")