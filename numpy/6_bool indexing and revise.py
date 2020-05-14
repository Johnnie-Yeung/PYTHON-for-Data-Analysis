import numpy as np
t = np.arange(24).reshape((4,6))
print(t)
print('-'*100)
t[:,2:4] = 0
print(t)

t = np.arange(24).reshape((4,6))
print('-'*100)
t[t<10] = 3
print(t)

t = np.arange(24).reshape((4,6))
# python的三元运算符
a = 3 if 3>2 else 4   # 结果为a = 3
# numpy的三元运算符
t = np.where(t<=3,100,300)
print(t)

t = np.arange(24).reshape((4,6))
t = t.clip(10,18)   # 裁剪
print(t)

t = np.arange(24).reshape((4,6))
t = t.astype(float)
t[3,3] = np.nan
print(t)