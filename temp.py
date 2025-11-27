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
            [364,0],
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

print(deg)
print(f"deg:{deg.shape}")
print(f"data:{data.shape}")
print(f"dt1:{dt1.shape}\ndt2:{dt2.shape}")