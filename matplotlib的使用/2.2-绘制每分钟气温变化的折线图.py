# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
# a= [random.randint(20,35) for i in range(120)]

# coding = utf-8
import random
from matplotlib import pyplot as plt
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=60)
plt.plot(x, y)
plt.xticks(range(0, 121, 5))
plt.yticks(range(20, 36))
plt.show()
