from matplotlib import pyplot as plt
x = range(11,31)
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

y_range = range(min(y_1+y_2),max(y_1+y_2)+1)
plt.figure(figsize=(16,8),dpi=70)

# 画两条线，可添加label、color、linestyle、linewidth等参数
# color参数也可以写颜色对应的16进制码
plt.plot(x,y_1,label='self',color='#DB7093',linestyle=':',linewidth=2.6)
plt.plot(x,y_2,label='friend',color='g',linestyle='-.')

plt.xticks(x)
plt.yticks(y_range)
plt.xlabel('age')
plt.ylabel('number')
plt.title('Trend of ??? number')

# 绘制网格
# alpha透明度，0~1
# 可添加linestyle、linewidth等参数
plt.grid(alpha=0.4,linestyle='--',linewidth=1.8)

# 添加图例
# 位置参数填字符串或数字都可以
plt.legend(loc='upper left')

plt.show()