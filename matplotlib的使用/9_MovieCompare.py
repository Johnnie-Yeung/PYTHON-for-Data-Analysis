# 假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,
# 为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?
from matplotlib import pyplot as plt
a = ["War for the Planet of the Apes","Dunkirk","Spider-Man:Homecoming","Wolf Warriors Ⅱ"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width for i in x_15]

plt.figure(figsize=(12,6))
plt.bar(x_14,b_14,width=bar_width,label='14th.September')
plt.bar(x_15,b_15,width=bar_width,label='15th.September')
plt.bar(x_16,b_16,width=bar_width,label='16th.September')

plt.xticks(x_15,a)
plt.legend()
plt.show()