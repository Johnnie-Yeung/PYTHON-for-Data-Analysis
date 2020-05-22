import pandas as pd
# Series一维，带标签数组
# DataFrame二维，Series容器
t = pd.Series([1,2,31,12,3,4])
print(t)
# 指定索引
t2 = pd.Series([1,23,2,2,1],index=list('abcde'))
print(t2)
print('-'*50)
temp_dict = {'name':'xiaohong', 'age':30, 'tel':10086}
t3 = pd.Series(temp_dict)
print(t3)
# 类型转换，与numpy方法一样
t2 = t2.astype(float)
print(t2)
print('-'*50)
# 索引和切片
print(t3['age'])
print(t3[0])
print(t3[:2])
print(t3[[1,2]])
print(t3[['age', 'tel']])
print(t[t>10])  # 布尔索引

print('-'*50)
print(t3.index)
for i in t3.index:
    print(i)
print(t3.values)