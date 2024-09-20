import os
import pandas as pd
from pyspark import SparkConf,SparkContext
os.environ['PYSPARK_PYTHON'] = "D:\Develop\python\python310\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc =SparkContext(conf = conf)

rdd = sc.textFile("D:\黑马代码\第15章资料\资料\search_log.txt")

#print(type(rdd.collect()))

#print(rdd.collect())
print(rdd.map(lambda line:line.split("\t")[0]).map(lambda x:x[0:2]).collect())


