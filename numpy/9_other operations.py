import numpy as np
a = np.zeros((3,4)).astype(int)
b = np.ones((2,3)).astype(int)
print(a)
print(b)

# 创建一个对角线全为1的方阵
t = np.eye(4).astype(int)
print(t)

print(np.argmax(t,axis=0))  # 获得每列(axis=0)的最大值的位置
print(np.argmin(t,axis=1))  # 获得每行(axis=1)的最小值的位置

# a=b是浅拷贝，a和b相互影响
# copy方法，a和b互不影响
a = b.copy()