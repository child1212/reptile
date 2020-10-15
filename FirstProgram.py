#%%
from bs4 import BeautifulSoup
import requests
import pymysql
from config import *


url_p = 'https://bj.ke.com/ershoufang/{area}/pg{num}/'
area = AREA
for i in range(1,100):
    print(i,end='\n')
    if i == 1:
        url = 'https://bj.ke.com/ershoufang/{area}/'.format(area=area)
    else:
        url = url_p.format(num=i,area=area)


    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')

    info_list = soup.find_all(attrs={"class" : "address"})

    db = pymysql.connect("localhost","root","123456","Houses")
    cur_insert = db.cursor()
    for info in info_list:
        try:
            ad = info.find_all(attrs={"class":"positionInfo"})
            addr = ad[0].get_text().replace('\n','')
            inf = info.find_all(attrs={"class":"houseInfo"})
            inf = inf[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',')
            inf = inf[1:-1]
            inf = inf.split(',')
            floor,year,typ,size,direction = inf[0],inf[1][:-2],inf[2],inf[3][:-2],inf[4]
            totalPrice = info.find_all(attrs={"class":"totalPrice"})
            total = totalPrice[0].get_text()
            unitPrice = info.find_all(attrs={"class":"unitPrice"})
            unit = unitPrice[0].get_text()[3:-5]
            sql_insert ="""insert into {area}_info(address,floor,year,size,type,direction,totalPrice,unitPrice) values (\"{address}\",\"{floor}\",\"{year}\",\"{size}\",\"{type}\",\"{direction}\",\"{totalPrice}\",\"{unitPrice}\")""".format(area=area,address=addr,floor=floor,year=year,type=typ,size=size,direction=direction,totalPrice=total,unitPrice=unit)
            print(addr,end=';')
        except:
            pass
        try:
            cur_insert.execute(sql_insert)
            # 提交
            db.commit()
            print('开始数据库插入操作',end=';')
        except Exception as e:
            db.rollback()
            print('数据库插入操作错误回滚')
    db.close()

# %%
