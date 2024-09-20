from pymysql import Connection

from pythonProject3.类和对象的综合案例体会.File_define import File_read1, File_read2

file_text = File_read1("D:\年1月销售数据.txt")
file_json = File_read2("D:\年2月销售数据JSON.txt")
data_record = file_text.read_data() + file_json.read_date()
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
#创建date,id,money,province表格
#cursor.execute('create table sell(date varchar(20),id varchar(255),money int,province varchar(20))')
#向数据库添加数据
for record in data_record:
    cursor.execute("insert into sell(date,id,money,province) values(%s, %s, %s, %s)",
                   (record.date, record.id_cord, record.money, record.province))
conn.close()

