# 假设你获取到了2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?

from matplotlib import pyplot as plt

a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

plt.figure(figsize=(16,8),dpi=80)
plt.bar(range(len(a)),b,width=0.3)
plt.xticks(range(len(a)),a)

plt.show()