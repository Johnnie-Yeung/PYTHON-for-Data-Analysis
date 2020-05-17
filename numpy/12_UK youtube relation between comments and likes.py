import numpy as np
from matplotlib import pyplot as plt
uk_file_path = 'E:/software/untitled/GB_video_data_numbers.csv'
t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype=int)
# 选择喜欢数比50万小的数据
t_uk = t_uk[t_uk[:,1] <= 500000]

t_uk_comment = t_uk[:,-1]
t_uk_like = t_uk[:,1]

plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comment)

plt.title('UK youtube relation between comments and likes')
plt.xlabel('likes number')
plt.ylabel('comments number')
plt.show()