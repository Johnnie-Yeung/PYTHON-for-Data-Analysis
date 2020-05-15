import numpy as np
us_data = 'E:/software/untitled/US_video_data_numbers.csv'
uk_data = 'E:/software/untitled/GB_video_data_numbers.csv'
# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=',', dtype=int)

# 构造全为0的数据
zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((uk_data.shape[0],1)).astype(int)

# 分别添加一列数据
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))
# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)