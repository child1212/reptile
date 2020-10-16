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

sql_2 = '''CREATE TABLE `chengjiao2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `xiaoqu` CHAR(40),
  `area` CHAR(40),
  `year` CHAR(40),
  `louceng` CHAR(40),
  `huxing` CHAR(40),
  `zhuangxiu` CHAR(40),
  `fangxiang` CHAR(40),
  `size` CHAR(40),
  `date` CHAR(40),
  `price` CHAR(40),
  `duration` CHAR(40),
  `subway` CHAR(40),
  `unitPrice` CHAR(40),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

sql_2 = sql_2.format(area=area)
#执行命令
cursor.execute(sql_2)

# %%
