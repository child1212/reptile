#%%
from bs4 import BeautifulSoup
import requests
import pymysql
from config import *

def get_total_count(url_p):
    r = requests.get(url_p)
    soup = BeautifulSoup(r.text,'lxml')
    info_list = soup.find_all(attrs={'class':"total fl"})
    info = info_list[0].get_text()
    return int(info.split(' ')[1])
for AREA in AREA_LIST:
    print(AREA)
    url_p = 'https://bj.ke.com/xiaoqu/{area}/'.format(area=AREA)
    total = get_total_count(url_p)
    if total % 30 == 0:
        pages = (total//30)
    else:
        pages = (total//30)+1
    for i in range(1,pages+1):
        print('\n',i,'/',pages)
    # for i in range(1,2):
        if i == 1:
            url = 'https://bj.ke.com/xiaoqu/{area}/'.format(area=AREA)
        else:
            url = 'https://bj.ke.com/xiaoqu/{area}/pg{num}/'.format(area=AREA,num=i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        info_list = soup.find_all(attrs={'class':'clear xiaoquListItem CLICKDATA'})

        # addr = info_list[0].find_all(attrs={'class':'positionInfo'})[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',').replace(',/',',')[1:-1:]
        # price = info_list[0].find_all(attrs={'class':'totalPrice'})[0].get_text()
        # subway = info_list[0].find_all(attrs={'class':'tagList'})[0].get_text()
        db = pymysql.connect("localhost","root","123456","Houses")
        cur_insert = db.cursor()
        for info in info_list:
            try:
                xiaoqu = info.find_all(attrs={'class':'title'})[0].get_text().replace('\n','')
                posi = info.find_all(attrs={'class':'positionInfo'})[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',').replace(',/',',')[1:-1:]
                inf = posi.split(',')
                addr,addr_1,typ,year = inf[0],inf[1],inf[2],inf[3]
                price = info.find_all(attrs={'class':'totalPrice'})[0].get_text().replace('\n','')
                subway = info_list[0].find_all(attrs={'class':'tagList'})[0].get_text().replace('\n','')
                sql_insert ="""insert into xiaoqu(xiaoqu,area,addr,type,year,price,subway) values (\"{xiaoqu}\",\"{addr}\",\"{addr_1}\",\"{typ}\",\"{year}\",\"{price}\",\"{subway}\")""".format(xiaoqu=xiaoqu,addr=addr,addr_1=addr_1,year=year,typ=typ,price=price,subway=subway)
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
