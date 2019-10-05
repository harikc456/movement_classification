# Movement Classification using Pyspark mllib
Classifying whether a person is walking or running from the data received from the accelerometer in our smartphone

# Files
 preprocess.py - used to preprocess the data and split it into train and test
 hdfs_preprocess.py - used to preprocess the data and split it into train and test after loading it from hadoop filesystem
 train.py - used to train a model and test it on test data
 
# Requirements
1) Python 2.7 <br>
2) Pyspark 2.4.4 <br>
3) Hadoop 3.1.2 <br>
4) Spark 2.4.4 <br>

# Instructions to run the code

Start Hadoop file system by running these commands in the terminal

<code>
start-dfs.sh <br>
start-yarn.sh
</code>

Open the terminal and run the following commands
<code><
spark-submit path/python_file.py                                                                                
</code>
 
