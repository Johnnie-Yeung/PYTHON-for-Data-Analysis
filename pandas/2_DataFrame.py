import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape((3,4)), index=list('abc'), columns=list('wxyz'))
print(t1)
# 传入字典
d1 = {'name':['xiaoming','xiaozhang'], 'age':[20,32], 'tel':[10086,10010]}
t1 = pd.DataFrame(d1)
print(t1)
# 传入列表
print('-'*100)
print('t2')
d2 = [{'name':'xiaohong', 'age':32, 'tel':10010}, {'name':'xiaozhang', 'tel':10000}, {'name':'xiaowang', 'age':22}]
t2 = pd.DataFrame(d2)
print(t2)
print('-'*100)

print(t2.index)
print(t2.columns)
print(t2.values)
print(t2.shape)
print(t2.dtypes)
print(t2.ndim)  # 维度
print('-'*100)

# 显示头几行
print(t2.head(1))
# 显示后几行
print(t2.tail(2))
print('-'*100)

# 展示DataFrame的概览
print(t2.info())
# 五数分析
print('-'*100)
print(t2.describe())