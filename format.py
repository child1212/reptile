#%%
f = open('E:\\chengjiao.txt','r',encoding='utf8')
fin = open('E:\\chengjiao1.txt','a',encoding='utf8')
for line in f:
    if '元/平' in line:
        t = line.replace('\\','')
    else:
        t = line.replace('\n','').replace('\\','')
    fin.write(t)
f.close()
fin.close()
print("finish")

# %%