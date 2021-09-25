#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

def confusionMatrix(actual_class, predicted_class):
    result = None

    # No: 1, Yes: 2

    if actual_class == 2 and predicted_class == 2:
        result = 'True Positive'
    elif actual_class == 2 and predicted_class == 1:
        result = 'False Negative'
    elif actual_class == 1 and predicted_class == 2:
        result = 'False Positive'
    elif actual_class == 1 and predicted_class == 1:
        result = 'True Negative'

    return result

def performanceCounter(result_tracker):
    num_TP = 0
    num_FP = 0
    num_FN = 0
    num_TN = 0

    for accuracy in result_tracker:
        if accuracy == 'True Positive':
            num_TP += 1
        elif accuracy == 'False Negative':
            num_FN += 1
        elif accuracy == 'False Positive':
            num_FP += 1
        elif accuracy == 'True Negative':
            num_TN += 1

    return num_TP, num_FP, num_FN, num_TN

def calculateAccuracy(result_tracker):
    num_TP, num_FP, num_FN, num_TN = performanceCounter(result_tracker)

    return (num_TP + num_TN) / (num_TP + num_TN + num_FP + num_FN)

file_prefix = ".\\data\\"

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(file_prefix+ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    values = {
        "Young":1, "Prepresbyopic":2, "Presbyopic":3, 
        "Myope":1, "Hypermetrope":2, 
        "No":1, "Yes":2, 
        "Reduced":1, "Normal":2
    }

    for row in dbTraining:
        new_row = []
        for value in row:
            new_row.append(values[value])
        X.append(new_row[:4])
        Y.append(new_row[4])

    lowest_accuracy = 9999

    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        ds_ = "contact_lens_test.csv"

        dbTest = []
        X_ = []
        Y_ = []

        with open(file_prefix+ds_, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)

        for row in dbTest:
            new_row = []
            for value in row:
                new_row.append(values[value])
            X_.append(new_row)

        
        result_tracker = []

        for data in X_:
            #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            class_predicted = clf.predict([data[:4]])[0]

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here

            result = confusionMatrix(data[4], class_predicted)
            result_tracker.append(result)

            #find the lowest accuracy of this model during the 10 runs (training and test set)
            #--> add your Python code here
        
        accuracy = calculateAccuracy(result_tracker)

        if accuracy < lowest_accuracy:
            lowest_accuracy = accuracy

    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here

    print(ds + ': ' + str(lowest_accuracy))


