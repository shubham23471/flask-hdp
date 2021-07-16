from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext("yarn", "flaskde_test", conf=conf)
hc = HiveContext(sc)
print("sc=", sc)
df = hc.sql("show databases")
print(df.show())
