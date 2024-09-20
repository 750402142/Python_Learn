from pyspark import SparkConf, SparkContext

#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
#基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf= conf)
#打印pyspark的运行版本
print(sc.version)
#停止SparkContext对象的运行(停止PySpark程序)
sc.stop()