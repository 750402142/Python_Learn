
from traceback import print_tb

from pyspark import SparkConf,SparkContext

import os
os.environ['PYSPARK_PYTHON'] = "D:\Develop\python\python310\python.exe"#你搞你爹呢

#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf= conf)

rdd = sc.parallelize([('男',20),('女',10),("男",10),("女",30),("女",20)])
rdd2 = rdd.reduceByKey(lambda x,y:x+y)

print(rdd2.collect())