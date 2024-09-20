from pymysql import Connection
#连接到数据库
conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '200520',
    autocommit = True#自动确认
)

#执行非查询性质SQL
cursor = conn.cursor() #获取到游标对象
#选择数据库
conn.select_db('practice')
#执行sql语言,创建图表
cursor.execute('create table student(id int,age int,name varchar(20))')
#确认所安装sql的版本号
#print(conn.get_server_info())
cursor.execute('insert into student values(001,10,"王尹"),(002,11,"尹王")')#向表中插入数据
#确认所执行的
#conn.commit()
#断开连接
conn.close()