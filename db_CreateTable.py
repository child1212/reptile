#%%
# python + pymysql 创建数据库 
import pymysql
from config import *

area = AREA
# 创建连接
conn = pymysql.connect(host='localhost',user='root',password='123456',charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
 
# 创建数据库的sql(如果数据库存在就不创建，防止异常)
sql = "CREATE DATABASE IF NOT EXISTS Houses" 
# 执行创建数据库的sql
cursor.execute(sql)

cursor.execute("use Houses;")

#创建数据表

# sql_2 = '''CREATE TABLE `{area}_info` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `address` CHAR(40),
#   `floor` CHAR(40),
#   `year` INT,
#   `type` CHAR(40),
#   `size` FLOAT,
#   `direction` CHAR(40),
#   `totalPrice` CHAR(40),
#   `unitPrice` FLOAT,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# '''

sql_2 = '''CREATE TABLE `chengjiao4` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `小区` CHAR(40),
  `城区` CHAR(40),
  `建成年代` CHAR(40),
  `所在楼层` CHAR(40),
  `房屋户型` CHAR(40),
  `装修情况` CHAR(40),
  `房屋朝向` CHAR(40),
  `建筑面积` CHAR(40),
  `成交时间` CHAR(40),
  `总价` CHAR(40),
  `房屋年限` CHAR(40),
  `地铁` CHAR(40),
  `单价` CHAR(40),
  `户型结构` CHAR(40),
  `套内面积` CHAR(40),
  `建筑类型` CHAR(40),
  `建筑结构` CHAR(40),
  `供暖方式` CHAR(40),
  `梯户比例` CHAR(40),
  `配备电梯` CHAR(40),
  `链家编号` CHAR(40),
  `交易权属` CHAR(40),
  `挂牌时间` CHAR(40),
  `房屋用途` CHAR(40),
  `房权所属` CHAR(40),


  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

sql_2 = sql_2.format(area=area)
#执行命令
cursor.execute(sql_2)

# %%
