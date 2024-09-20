from traceback import print_tb

from pyspark import SparkConf,SparkContext

import os
os.environ['PYSPARK_PYTHON'] = "D:\Develop\python\python310\python.exe"#你搞你爹呢
os.environ["HADOOp_HOME"]  = "D:\Develop\hadoop\hadoop-3.0.0"
#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf= conf)
#打印pyspark的运行版本
#print(sc.version)
rdd = sc.textFile("D:\pylearn\work\datas.txt")
rdd2 = sc.parallelize([4,5,9])
rdd3 = rdd2.map(lambda x:x*10)
print(rdd3.collect())
#print(type(rdd.collect()))
#停止SparkContext对象的运行(停止PySpark程序)
#save的使用
rdd4 = sc.parallelize([1,34,43,92],1)#后面加个1是为了只生成一个文件
rdd4.saveAsTextFile("D:\pylearn\work\data2.txt")
sc.stop()
