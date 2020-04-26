from matplotlib import pyplot as plt
import random
x = range(0,120)
y = [random.randint(20,35) for i in range(0,120)]
plt.figure(figsize=(20,8), dpi=60)
plt.plot(x,y)

# 调整x轴和y轴的刻度
y_range = range(min(y),max(y))  # y的取值范围
_xtick_labels = ['10:{}'.format(i) for i in range(60)] + ['11:{}'.format(i) for i in range(60)]
_ytick_labels = ['{}℃'.format(i) for i in y_range]
plt.xticks(list(x)[::5],_xtick_labels[::5],rotation=45)    # 第二个参数与第一个参数一一对应，可以让数字与字符串一一对应,rotation参数是x轴的刻度旋转的度数
plt.yticks(y_range[::2],_ytick_labels[::2])

# 添加描述信息
plt.xlabel('Time')       # 设置x轴标签
plt.ylabel('Temperature')   # 设置y轴标签
plt.title('Temperature between 10:00-12:00')   # 标题

plt.show()