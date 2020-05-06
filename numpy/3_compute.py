import numpy as np
t5 = np.arange(0,24).reshape((4,6))
print('t5:')
print(t5)
print('t5+2:')
print(t5+2)  # 广播计算，数组的数值计算，加减乘除都可以

t6 = np.arange(100,124).reshape((4,6))
print('t6+t5:')
print(t6+t5)  # 数组间进行计算，加减乘除都可以，对应位置数值进行计算

# 数组间进行计算需要至少一个维度的数量是相同的
t7 = np.arange(0,6)
print('t5-t7:')
print(t5-t7)

t8 = np.arange(4).reshape((4,1))
print('t5-t8:')
print(t5-t8)