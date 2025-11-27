import numpy as np
from scipy.optimize import approx_fprime

data = np.zeros((4,6,2))

data[0] = ([[302,23],
            [309,4],
            [307,19],
            [307,28],
            [312,45],
            [314,26]])

data[1] = ([[122,24],
            [129,5],
            [127,21],
            [127,30],
            [132,46],
            [134,26]])

data[2] = ([[353,56],
            [361,12],
            [358,45],
            [358,54],
            [364,42],
            [365,55]])

data[3] = ([[173,58],
            [181,11],
            [178,45],
            [178,43],
            [184,42],
            [185,54]])

# print(data[...,0])
deg = data[:,:,0]+data[...,1]/60

dt1 = deg[2,...]-deg[0,...]
dt2 = deg[3,...]-deg[1,...]

resu = 0.5*(dt1+dt2)
# print(dt1,'\n',dt2)
print(resu)
print("-------------------------------")
print("最小偏向角: ",np.mean(resu))
uncertain_A = np.sqrt(np.var(resu,ddof=1))
print("A类不确定度: ",uncertain_A)
uncertain_B  = 1/60
uncertain = np.sqrt((np.pow(uncertain_A,2)+np.pow(uncertain_B,2)/2))

print("不确定度: ",uncertain)
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
print(f"折射率的不确定度{partial_y*uncertain}")
error = (partial_y*uncertain/n)*100
print(f"相对误差为：{error}%")