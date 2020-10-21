#%%
from bs4 import BeautifulSoup
import requests
import pymysql
import random
import time
from config import *


# AREA = 'yanqing'
start = 1
# db = 'Houses'
table = 'chengjiao3'

run = start
while run < 101:
    print('\n==========================================>',run)
    if run == 1:
        url = 'https://bj.ke.com/chengjiao/'
    else:
        url = 'https://bj.ke.com/chengjiao/pg{num}/'.format(num=run)
    r = 0
    while r == 0:
        try:
            r = requests.get(url,timeout=1)
        except:
            pass
    soup = BeautifulSoup(r.text,'lxml')
    info_list = soup.find_all(attrs={'class':'info'})
    if len(info_list) == 0:
        print('hello world')
        input()
        continue

    db = pymysql.connect("localhost","root","123456",'Houses')
    cur_insert = db.cursor()
    for info in info_list:
        #获取详细信息
        print('获取详细信息',end=';')
        url_detail = info.find_all('a')[0]['href']

        rr = 0
        while rr == 0:
            try:
                rr = requests.get(url_detail,timeout=1)
            except:
                pass

        ssoup = BeautifulSoup(rr.text,'lxml')
        info_llist = ssoup.find_all(attrs={'class':'introContent'})
        if len(info_llist) == 0:
            print('hello world')
            input()
            continue
        infomation = dict()
        for iinfo in info_llist:
            info_detail = iinfo.find_all('li')
            for detail in info_detail:
                key = detail.get_text()[:4]
                value = detail.get_text()[4:].replace(' ','')
                infomation[key] = value
        # 获取概况
        print('获取概况',end=';')
        mass = info.find_all(attrs={'class':'title'})[0].get_text().replace('\n','').split(' ')
        try:
            sub = info.find_all(attrs={'class':'dealHouseTxt'})[0].get_text().replace('\n','').replace('五年','五年,').replace('两年','两年,').split(',')
        except:
            sub = ['','']
        xiaoqu = mass[0]
        date = info.find_all(attrs={'class':'dealDate'})[0].get_text().replace('\n','').replace(" ",'')
        price = info.find_all(attrs={'class':'totalPrice'})[0].get_text().replace('\n','').replace(" ",'')
        if len(sub) == 1:
            subway = sub[0]
        else:
            subway = sub[1]
        unitPrice = info.find_all(attrs={"class":"unitPrice"})[0].get_text().replace(' ','')
        sql = "select area from xiaoqu where xiaoqu = '{xiaoqu}';".format(xiaoqu = xiaoqu)
        cur_insert.execute(sql)
        print('area',end=';')
        try:
            area = cur_insert.fetchall()[0][0]
        except:
            area = ''
        duration = infomation['房屋年限']
        size = infomation['建筑面积']
        year = infomation['建成年代']
        louceng = infomation['所在楼层']
        huxing = infomation['房屋户型']
        zhuangxiu = infomation['装修情况']
        fangxiang = infomation['房屋朝向']
        huxingjiegou = infomation['户型结构']
        taonei = infomation['套内面积']
        leixing = infomation['建筑类型']
        jianzhujiegou = infomation['建筑结构']
        gongnuan = infomation['供暖方式']
        tihu = infomation['梯户比例']
        dianti = infomation['配备电梯']
        liangjia = infomation['链家编号']
        quanshu = infomation['交易权属']
        gpshijian = infomation['挂牌时间']
        yongtu = infomation['房屋用途']
        fangquan = infomation['房权所属']

        sql_insert ="""insert into {table}(小区,城区,建成年代,所在楼层,房屋户型,装修情况,房屋朝向,建筑面积,总价,房屋年限,地铁,单价,成交时间,户型结构,套内面积,建筑类型,建筑结构,供暖方式,梯户比例,配备电梯,链家编号,交易权属,挂牌时间,房屋用途,房权所属) values (\"{xiaoqu}\",\"{area}\",\"{year}\",\"{louceng}\",\"{huxing}\",\"{zhuangxiu}\",\"{fangxiang}\",\"{size}\",\"{price}\",\"{duration}\",\"{subway}\",\"{unitPrice}\",\"{date}\",\"{huxingjiegou}\",\"{taonei}\",\"{leixing}\",\"{jianzhujiegou}\",\"{gongnuan}\",\"{tihu}\",\"{dianti}\",\"{liangjia}\",\"{quanshu}\",\"{gpshijian}\",\"{yongtu}\",\"{fangquan}\")""".format(xiaoqu=xiaoqu,area=area,year=year,louceng=louceng,huxing=huxing,zhuangxiu=zhuangxiu,fangxiang=fangxiang,size=size,price=price,duration=duration,subway=subway,unitPrice=unitPrice,date=date,table=table,huxingjiegou=huxingjiegou,taonei=taonei,leixing=leixing,jianzhujiegou=jianzhujiegou,gongnuan=gongnuan,tihu=tihu,dianti=dianti,liangjia=liangjia,quanshu=quanshu,gpshijian=gpshijian,yongtu=yongtu,fangquan=fangquan)
        if date > '2020.10.04':
            try:
                cur_insert.execute(sql_insert)
                # 提交
                db.commit()
                print('开始数据库插入操作',end=';\n')
            except Exception as e:
                db.rollback()
                print('数据库插入操作错误回滚')
        else:
            run = 101
    db.close()
    run += 1
print("finish")



# %%
