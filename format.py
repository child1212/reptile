#%%
#小区,城区,建成年代,所在楼层,房屋户型,装修情况,房屋朝向,建筑面积,成交时间,总价,房屋年限,地铁,单价,户型结构,套内面积,建筑类型,建筑结构,供暖方式,梯户比例,配备电梯,链家编号,交易权属,挂牌时间,房屋用途,房权所属
f = open('E:\\chengjiao.txt','r')
fin = open('E:\\chengjiao1.txt','a')
i = 0
for line in f:
    if i%4 == 0:
        t = line.replace('\\','')
        i = 0
    else:
        t = line.replace('\n','').replace('\\','')
    fin.write(t)
    i += 1
f.close()
fin.close()
print("finish")

# %%

# %%
