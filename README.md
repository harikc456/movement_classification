# Motion Classification using Pyspark mllib
Classifying whether a person is walking or running from the data received from the accelerometer in our smartphone

# Files
 preprocess.py - used to preprocess the data and split it into train and test <br>
 hdfs_preprocess.py - used to preprocess the data and split it into train and test after loading it from hadoop filesystem <br>
 train.py - used to train a model and test it on test data <br>
 
# Requirements
1) Python 2.7 <br>
2) Pyspark 2.4.4 <br>
3) Hadoop 3.1.2 <br>
4) Spark 2.4.4 <br>

# Instructions to run the code
You can skip the first two commands if you are not using HDFS

Start Hadoop file system by running these commands in the terminal
<br>
<code>
start-dfs.sh 
</code>

Start yarn using the below command
<br>
<code>
start-yarn.sh
</code>

Open the terminal and run the following commands
If you're using hdfs use the below command
<br>
<code>
spark-submit hdfs_preprocess.py                                                                               
</code>

If you've the file locally, then run the preprocess.py file
<br>
<code>
spark-submit preprocess.py                                                                               
</code>

Train and save the model by the below command
<br>
<code>
spark-submit train.py                                                                               
</code>
 
