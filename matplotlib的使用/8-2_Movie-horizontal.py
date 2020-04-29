# 假设你获取到了2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?
# 绘制横着的条形图
from matplotlib import pyplot as plt

a = ["Wolf Warriors Ⅱ","The Fate of the Furious 8","Kung Fu Yoga","Journey to the West:The Demons Strike Back","Transformers:The Last Knight","Dangal","Pirates of the Caribbean:Dead Men Tell No Tales/Salazar's Revenge","Kong:Skull Island","xXx:Return of Xander Cage","Resident Evil: The Final Chapter","Duckweed","Despicable Me 3","The Taking of Tiger Mountain 3D","Buddies in India","Logan","Spider-Man:Homecoming","Wukong","Guardians of the Galaxy Vol.2","Qing Sheng","The Mummy"]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

plt.figure(figsize=(16,10),dpi=80)
plt.barh(range(len(a)),b,height=0.3,color='orange')
plt.yticks(range(len(a)),a)

plt.grid(alpha=0.3)
plt.xlabel('Box Office')
plt.ylabel('Movie')

plt.show()