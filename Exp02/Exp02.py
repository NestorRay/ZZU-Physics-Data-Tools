import numpy as np
once = np.array([723,683,46.56])    #这个数组的数据存放的是一次测量量L,H,D 单位是mm

def youngs(var):
    k,L,H,D,d = var
    a = (8*9.8*L*H)
    b = (np.pi*np.pow(d,2)*D*k)
    return a/b
# 钢丝直径d
d = np.array([1.088,
                     1.09,
                     1.12,
                     1.092,
                     1.09,
                     1.102])

#螺旋测微器的零差
d0 = 0.45

data = np.zeros((4,10))
# 这一维存放m的数据
data[0] = ([0,
            1.01,
            2.01,
            3.01,
            4.01,
            5.00,
            6.00,
            7.01,
            8.00,
            9.01])
# 这一维存放加力过程中的标尺读数
data[1] = ([13.9,
            17.0,
            20.4,
            23.8,
            27.0,
            30.1,
            33.2,
            36.7,
            39.9,
            43.1])
# 这一维存放减力过程中的标尺读数
data[2] = ([14.0,
            17.3,
            20.5,
            23.8,
            27.0,
            30.3,
            33.8,
            36.9,
            40.1,
            43.5])
# 这一维计算加减力过程中标尺读数的均值
data[3] = (data[1,...]+data[2,...])/2

# 预处理各数据化为国际单位制
data[1:4,...] = data[1:4,...]/1000
once = once/1000
d = d/1000
d0 = d0/1000

# 以下计算杨氏模量
diameter = np.mean(d) - d0
k,b = np.polyfit(data[0],data[3],deg=1)
input_data = np.concatenate([np.array([k]),once[:],np.array([diameter])])
result = youngs(input_data)
print(f"杨氏模量{result:.3e}")


# 以下开始计算不确定度
# 直径d的不确定度
uncertainty_d_A = 1.05 * np.std(d,ddof=1)
uncertainty_d_B = 0.004/1000
uncertainty_d = np.sqrt(uncertainty_d_A ** 2 + uncertainty_d_B ** 2)
relative_uncertainty_d = uncertainty_d/diameter

# x的不确定度
uncertainty_x_A = 1.24 * np.std(data[3],ddof=1)
uncertainty_x_B = 0.5 /1000
uncertainty_x = np.sqrt(uncertainty_x_A ** 2 + uncertainty_x_B ** 2)
relative_uncertainty_x = uncertainty_x/

#L, H, D, F的不确定度
uncertainty_L = 0.8/1000
uncertainty_H = 0.8/1000
uncertainty_D = 0.02/1000
uncertainty_F = 0.005 * 9.8

# 求相对不确定度
relative_uncertainy = np.sqrt()

# def uncertainty(var):
#     return np.sqrt()