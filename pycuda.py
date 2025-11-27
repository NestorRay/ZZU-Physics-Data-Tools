# test_gpu_working.py
import cupy as cp
import numpy as np

def test_cupy():
    print("=== CuPy基础测试 ===")
    
    # 测试1: 基础数组操作
    try:
        x = cp.array([1, 2, 3])
        y = cp.array([4, 5, 6])
        z = x + y
        print(f"✓ 基础运算: {cp.asnumpy(z)}")
    except Exception as e:
        print(f"✗ 基础运算失败: {e}")
        return False
    
    # 测试2: 矩阵乘法
    try:
        a = cp.random.rand(100, 100)
        b = cp.random.rand(100, 100)
        c = cp.dot(a, b)
        print(f"✓ 矩阵乘法: 成功创建 {c.shape} 矩阵")
    except Exception as e:
        print(f"✗ 矩阵乘法失败: {e}")
        return False
    
    # 测试3: 设备信息
    try:
        device_count = cp.cuda.runtime.getDeviceCount()
        print(f"✓ 找到 {device_count} 个GPU设备")
        for i in range(device_count):
            props = cp.cuda.runtime.getDeviceProperties(i)
            print(f"  设备 {i}: {props['name'].decode()}")
    except Exception as e:
        print(f"✗ 设备信息获取失败: {e}")
    
    return True

if __name__ == "__main__":
    test_cupy()