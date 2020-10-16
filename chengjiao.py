#%%
from bs4 import BeautifulSoup
import requests
import pymysql
import random
import time
from config import *

def get_total_count(url_p):
    r = requests.get(url_p)
    soup = BeautifulSoup(r.text,'lxml')
    info_list = soup.find_all(attrs={'class':"total fl"})
    info = info_list[0].get_text()
    return int(info.split(' ')[1])
for AREA in AREA_LIST:
    print(AREA)
    url_p = 'https://bj.ke.com/chengjiao/{area}/'.format(area=AREA)
    total = get_total_count(url_p)
    if total % 30 == 0:
        pages = (total//30)
    else:
        pages = (total//30)+1
    pages = min(pages,100)
    for i in range(1,pages+1):
        time.sleep(random.randint(0, 16))
        print('\n',i,'/',pages)
    # for i in range(1,2):
        if i == 1:
            url = 'https://bj.ke.com/chengjiao/{area}/'.format(area=AREA)
        else:
            url = 'https://bj.ke.com/chengjiao/{area}/pg{num}/'.format(area=AREA,num=i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        info_list = soup.find_all(attrs={'class':'info'})

        # addr = info_list[0].find_all(attrs={'class':'positionInfo'})[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',').replace(',/',',')[1:-1:]
        # price = info_list[0].find_all(attrs={'class':'totalPrice'})[0].get_text()
        # subway = info_list[0].find_all(attrs={'class':'tagList'})[0].get_text()
        db = pymysql.connect("localhost","root","123456","Houses")
        cur_insert = db.cursor()
        for info in info_list:
            try:
                # xiaoqu = info.find_all(attrs={'class':'title'})[0].get_text().replace('\n','')
                # posi = info.find_all(attrs={'class':'positionInfo'})[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',').replace(',/',',')[1:-1:]
                # inf = posi.split(',')
                # addr,addr_1,typ,year = inf[0],inf[1],inf[2],inf[3]
                mass = info.find_all(attrs={'class':'title'})[0].get_text().replace('\n','').split(' ')
                sub = info.find_all(attrs={'class':'dealHouseTxt'})[0].get_text().replace('\n','').replace('年','年,').split(',')
                houseInfo = info.find_all(attrs={'class':'houseInfo'})[0].get_text().replace('\n','').replace(' ','').split('|')
                positionInfo = info.find_all(attrs={'class':'positionInfo'})[0].get_text().replace('\n','').replace(' ','').replace(')','),').split(',')


                xiaoqu = mass[0]
                year = positionInfo[1]
                louceng = positionInfo[0]
                huxing = mass[1]
                zhuangxiu = houseInfo[1]
                fangxiang = houseInfo[0]
                size = mass[2]
                date = info.find_all(attrs={'class':'dealDate'})[0].get_text().replace('\n','').replace(" ",'')
                price = info.find_all(attrs={'class':'totalPrice'})[0].get_text().replace('\n','').replace(" ",'')
                duration = sub[0]
                subway = sub[1]
                unitPrice = info.find_all(attrs={"class":"unitPrice"})[0].get_text().replace(' ','')

                sql_insert ="""insert into chengjiao(xiaoqu,area,year,louceng,huxing,zhuangxiu,fangxiang,size,price,duration,subway,unitPrice,date) values (\"{xiaoqu}\",\"{area}\",\"{year}\",\"{louceng}\",\"{huxing}\",\"{zhuangxiu}\",\"{fangxiang}\",\"{size}\",\"{price}\",\"{duration}\",\"{subway}\",\"{unitPrice}\",\"{date}\")""".format(xiaoqu=xiaoqu,area=AREA,year=year,louceng=louceng,huxing=huxing,zhuangxiu=zhuangxiu,fangxiang=fangxiang,size=size,price=price,duration=duration,subway=subway,unitPrice=unitPrice,date=date)
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
print("finish")




# %%
