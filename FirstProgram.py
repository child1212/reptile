#%%
from bs4 import BeautifulSoup
import requests
import pymysql




url = 'https://bj.ke.com/ershoufang/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

info_list = soup.find_all(attrs={"class" : "address"})

db = pymysql.connect("localhost","root","123456","Houses")
cur_insert = db.cursor()
id = 0
for info in info_list:
    ad = info.find_all(attrs={"class":"positionInfo"})
    addr = ad[0].get_text()
    inf = info.find_all(attrs={"class":"houseInfo"})
    inf = inf[0].get_text().replace('\n','\t').replace('\t',',').replace('|',',').replace(' ','').replace(',,',',')
    inf = inf[1:-1]
    inf = inf.split(',')
    floor,year,typ,size,direction = inf[0],inf[1],inf[2],inf[3],inf[4]
    totalPrice = info.find_all(attrs={"class":"totalPrice"})
    total = totalPrice[0].get_text()
    unitPrice = info.find_all(attrs={"class":"unitPrice"})
    unit = unitPrice[0].get_text()
    sql_insert ="""insert into house_info(address,floor,year,size,type,direction,totalPrice,unitPrice) values (\"{address}\",\"{floor}\",\"{year}\",\"{size}\",\"{type}\",\"{direction}\",\"{totalPrice}\",\"{unitPrice}\")""".format(address=addr,floor=floor,year=year,type=typ,size=size,direction=direction,totalPrice=total,unitPrice=unit)
    print(sql_insert)
    try:
        cur_insert.execute(sql_insert)
        # 提交
        db.commit()
        print('开始数据库插入操作')
    except Exception as e:
        db.rollback()
        print('数据库插入操作错误回滚')
    id += 1
db.close()
#


