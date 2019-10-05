from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.master("local[2]").getOrCreate() 
spark.sparkContext.setLogLevel("ERROR")

# replace the path your hdfs path below
 
df1 = spark.read.csv('hdfs://localhost:54310/use_case/data.csv',header=True)

columns_to_be_dropped = ['Time (s)','Absolute acceleration (m/s^2)']

df1 = df1.drop(*columns_to_be_dropped)

print(df1.count())

df1 = df1.randomSplit([0.75,0.25])
df1[0].toPandas().to_csv('train.csv',index = False)
df1[1].toPandas().to_csv('test.csv',index = False)
