# coding = utf-8
from matplotlib import pyplot as plt
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
# figsize为可选参数，整数元组，（宽，高）
# 在图像模糊的时候可以传入dpi参数，让图片更加清晰，dpi表示该窗口的分辨率
plt.figure(figsize=(20, 8), dpi=60)


# 绘图
plt.plot(x, y)


# 绘制x轴的刻度
# range步长只能为整数，如果要小数，则要自己传个列表或用numpy.arange(2,25,0.5)
# plt.xticks(x)    # 1
# plt.xticks(range(2, 25))     # 2
_xtick_labels = [i/2 for i in range(4,49)]       # 3
plt.xticks(_xtick_labels[::3])       # 列表取步长
plt.yticks(range(min(y), max(y)+1))


# 保存图片
# 若show()之后保存，则会是空白，因为show()之后会创建新的画布
# 可以指定路径保存，如'C:/User/pic.png'，但是要注意跟windows系统的路径斜杠(\)是反的
# 也可保存为.pdf、.svg（矢量图）等格式
plt.savefig('hello.png')


# 展示图形
plt.show()
