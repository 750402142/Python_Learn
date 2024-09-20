from traceback import print_tb

'''
需求,复制以上内容到文件中,使用Spark读取文件进行计算
1.各个城市销售额排名，从大到小
2.全部城市,有哪些商品类别在售卖
3.北京市有哪些商品类别在售卖
'''
from pyspark import SparkConf,SparkContext
import json
import os
os.environ['PYSPARK_PYTHON'] = "D:\Develop\python\python310\python.exe"#你搞你爹呢
#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf= conf)

rdd = sc.textFile("D:\黑马代码\第15章资料\资料\orders.txt")
#得到的是json字符串的形式
rdd_json = rdd.flatMap(lambda line: line.split("|"))
#将json转为python形式的字典
rdd_dict = rdd_json.map(lambda x:json.loads(x))
rdd_request1 = rdd_dict.map(lambda x:(x["areaName"],int(x["money"]))).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1])
print(f"需求1: {rdd_request1.collect()}")
rdd_request2 = rdd_dict.map(lambda x:(x["category"])).distinct().collect()
print(f"需求2:{rdd_request2}")
rdd_request3 = rdd_dict.filter(lambda x:x["areaName"] == '北京').map(lambda x: x["category"]).distinct()
print(f"需求3:{rdd_request3.collect()}")
#print(rdd.collect())
sc.stop()

