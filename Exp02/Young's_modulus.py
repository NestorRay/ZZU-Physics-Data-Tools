import numpy as np
once = np.array([723,683,46.56])

def youngs(var):
    k,L,H,D,d = var
    a = (8*9.8*L*H)
    b = (np.pi*np.pow(d,2)*D*k)
    return a/b

diameter = np.array([1.088,
                     1.09,
                     1.12,
                     1.092,
                     1.09,
                     1.102])

d0 = 0.45
diameter = diameter-d0

data = np.zeros((4,10))
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

data[3] = (data[1,...]+data[2,...])/2

data[1:4,...] = data[1:4,...]/1000
once = once/1000
diameter = diameter/1000

k,b = np.polyfit(data[0],data[3],deg=1)
input_data = np.concatenate([np.array([k]),once[:],np.array([np.mean(diameter)])])
result = youngs(input_data)
print(f"杨氏模量{result:.3e}")