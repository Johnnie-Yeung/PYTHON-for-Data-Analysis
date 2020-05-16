import numpy as np
from matplotlib import pyplot as plt
us_file_path = 'E:/software/untitled/US_video_data_numbers.csv'
t_us = np.loadtxt(us_file_path,delimiter=',',dtype=int)

# 取评论数据
t_us_comment = t_us[:,-1]

# 选择比5000小的数据
t_us_comment = t_us_comment[t_us_comment <= 5000]

_xticks_ = range(0,5001,250)

plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comment,_xticks_)

plt.grid()
plt.title('US youtube comments statistics')
plt.xticks(_xticks_)
plt.ylabel('video numbers')
plt.xlabel('comment numbers')

plt.show()
