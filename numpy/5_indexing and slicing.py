# 现在这里有一个英国和美国各自youtube1000多个视频的点击,喜欢,不喜欢,评论数量(["views","likes","dislikes","comment_total"])的csv,
# 运用刚刚所学习的知识,我们尝试来对其进行操作

import numpy as np
us_file_path = 'E:/software/untitled/US_video_data_numbers.csv'
uk_file_path = 'E:/software/untitled/GB_video_data_numbers.csv'
# loadtxt读取csv文件,delimiter分隔符，unpack矩阵转置
t2 = np.loadtxt(us_file_path, delimiter=',', dtype=int)

print(t2)
print('*'*100)
# 取行
print(t2[2])

# 取连续的多行
print(t2[2:])

# 取不连续的多行
print(t2[[2,8,10]])

# 取列
print(t2[1,:])  # 逗号前表示行，后表示列，  :表示取所有列
print(t2[2:,:])
print(t2[[2,10,3],:])
print(t2[:,0])

# 取连续的多列
print(t2[:,2:])

# 取不连续的多列
print(t2[:,[0,2]])

# 取行和列
print(t2[2,3])

# 取多行和多列，取行和列相交的位置
#print(t2[2:5,1:4])

# 取多个不相邻的点
# 取出(0,0) (2,1) (2,3)的点
c = t2[[0,2,2],[0,1,3]]
print(c)
