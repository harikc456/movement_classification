from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark import SparkContext

def parsePoint(line):
    values = []
    for x in line.split(','):
        try:
            values.append(float(x))
        except:
            pass
    return LabeledPoint(array(values[3]), array([values[i] for i in (0,1,2)]))


sc = SparkContext("local[2]",'ML_1')
sc.setLogLevel("ERROR")
# Load train data

train_data = sc.textFile("train.csv")
#header = train_data.first()
#train_data = train_data.filter(lambda x: x != header)
train_data = train_data.filter(lambda x: "Linear Acceleration x (m/s^2)" not in x)
#print(train_data.take(5))
train_parsedData = train_data.map(parsePoint)

# Load test data

test_data = sc.textFile("test.csv")
#header = test_data.first()
test_data = test_data.filter(lambda x: "Linear Acceleration x (m/s^2)" not in x)
#print(test_data.take(5))
test_parsedData = test_data.map(parsePoint)

# Build LogisitcRegression Model
model = LogisticRegressionWithSGD.train(train_parsedData)

# Evaluating the model on training data
labelsAndPreds = train_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda (v, p): v == p).count() / float(train_parsedData.count())
print("LogisticRegression Accuracy on Training Data = " + str(trainAcc))

# Evaluating the model on testing data
labelsAndPreds = test_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda (v, p): v == p).count() / float(test_parsedData.count())
print("LogisticRegression on Test Data= " + str(trainAcc))

# Build the LogisitcRegressionLBFGS model
model = LogisticRegressionWithLBFGS.train(train_parsedData)

# Evaluating the model on training data
labelsAndPreds = train_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda lp: lp[0] == lp[1]).count() / float(train_parsedData.count())
print("LogisticRegressionWithLBFGS on Training Data = " + str(trainAcc))

# Evaluating the model on testing data
labelsAndPreds = test_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda (v, p): v == p).count() / float(test_parsedData.count())
print("LogisticRegressionWithLBFGS on Test Data = " + str(trainAcc))


# Build the SVM model
model = SVMWithSGD.train(train_parsedData, iterations=100)

# Evaluating the model on training data
labelsAndPreds = train_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda lp: lp[0] == lp[1]).count() / float(train_parsedData.count())
print("SVM Accuracy on Training Data = " + str(trainAcc))

# Evaluating the model on testing data
labelsAndPreds = test_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainAcc = labelsAndPreds.filter(lambda (v, p): v == p).count() / float(test_parsedData.count())
print("SVM Accuracy on Test Data = " + str(trainAcc))

# Saving the model
try:
    model.save(sc, "model/pythonSVMWithSGDModel")
except:
    pass
