#%%
# python + pymysql 创建数据库 
import pymysql
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
sql_2 = '''CREATE TABLE `house_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` CHAR(40),
  `floor` CHAR(40),
  `year` CHAR(40),
  `type` CHAR(40),
  `size` CHAR(40),
  `direction` CHAR(40),
  `totalPrice` CHAR(40),
  `unitPrice` CHAR(40),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
#执行命令
cursor.execute(sql_2)
