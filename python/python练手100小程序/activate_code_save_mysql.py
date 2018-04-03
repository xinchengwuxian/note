from activate_code_gen_2 import generate 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("10.190.23.206","root","root","datatest" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS ACTIVATECODE") 
# 使用预处理语句创建表
sql = """CREATE TABLE ACTIVATECODE (
         CODE  CHAR(22))"""

cursor.execute(sql)

codes = generate(200)
print(codes)

# SQL 插入语句
for code in codes:
    sql = """INSERT INTO ACTIVATECODE(CODE)
         VALUES ('{}')""".format(code)
    try:
    # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
    # 如果发生错误则回滚
        db.rollback()
 
# 关闭数据库连接
db.close()
# print(generate(200))
