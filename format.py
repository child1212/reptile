#%%
f = open('E:\\chengjiao-detail.txt','r',encoding='utf8')
fin = open('E:\\chengjiao.txt','a',encoding='utf8')
i = 1
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
