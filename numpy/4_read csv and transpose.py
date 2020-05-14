# 现在这里有一个英国和美国各自youtube1000多个视频的点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv,
# 运用刚刚所学习的知识,我们尝试来对其进行操作

import numpy as np
us_file_path = 'E:/software/untitled/US_video_data_numbers.csv'
uk_file_path = 'E:/software/untitled/GB_video_data_numbers.csv'
# loadtxt读取csv文件,delimiter分隔符，unpack矩阵转置
t1 = np.loadtxt(us_file_path, delimiter=',', dtype='int', unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=',', dtype='int')

print(t1)
print('*'*100)
print(t2)

t3 = np.arange(24).reshape((4,6))
print('-'*50)
print(t3)
# 矩阵转置的三种方法
print(t3.transpose())  # 转置
print(t3.T)            # 大写T表示转置
print(t3.swapaxes(1,0))  # 交换轴