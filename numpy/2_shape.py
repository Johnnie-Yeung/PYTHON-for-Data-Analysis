import numpy as np
t1 = np.arange(12)
print(t1)
print(t1.shape)

print('-'*50)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

print('-'*50)

t3 = np.array( [ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]] ] )
print(t3)
print(t3.shape)

print('-'*50)

# 使用reshape方法，t4本身不发生变化，reshape是提供一个返回值
t4 = np.arange(12)
t4 = t4.reshape((3,4))
print(t4)

print('-'*50)

t5 = np.arange(24).reshape((2,3,4))
print(t5)
t5 = t5.reshape((4,6))
print(t5)
print(t5.reshape((1,24)))
print(t5.reshape((24,)))
print(t5.reshape(-1))
print(t5.flatten())  # 展开成一维