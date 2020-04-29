# 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?

from matplotlib import pyplot as plt
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1, 32)
x_10 =range(51, 82)
y_range = range(min(y_3 + y_10), max(y_3 + y_10)+1)
plt.figure(figsize=(20, 8), dpi=70)

plt.scatter(x_3,y_3,label='March')
plt.scatter(x_10,y_10,label='October')

_x = list(x_3) + list(x_10)
_xtick_labels = ["3.{}".format(i) for i in x_3] + ["10.{}".format(i) for i in x_3]
plt.xticks(_x[::2], _xtick_labels[::2], rotation=40)
plt.yticks(y_range[::2])

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Title')

plt.legend()
plt.show()