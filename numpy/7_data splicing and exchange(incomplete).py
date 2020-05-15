import numpy as np
us_file_path = 'E:/software/untitled/US_video_data_numbers.csv'
uk_file_path = 'E:/software/untitled/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int')
t2 = np.loadtxt(uk_file_path,delimiter=',',dtype='int')
# 垂直拼接 vertically
np.vstack((t1,t2))
# 水平拼接 horizontally
np.hstack((t1,t2))

# 行交换
t[[1,2],:] = t[[2,1],:]
# 列交换
t[:,[0,2]] = t[:,[2,0]]