from traceback import print_tb

from pyspark import SparkConf,SparkContext

import os
os.environ['PYSPARK_PYTHON'] = "D:\Develop\python\python310\python.exe"#你搞你爹呢
#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf= conf)
rdd = sc.textFile("D:\黑马代码\第15章资料\资料\hello.txt")
word_rdd = rdd.flatMap(lambda x: x.split(' '))#split方法切割后生成的是一个个列表,用flatmap来解除列表的嵌套
#print(rdd.collect())
word_simple_rdd = word_rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1])
print(word_simple_rdd.collect())
sc.stop()

