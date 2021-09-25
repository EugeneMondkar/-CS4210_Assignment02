#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries

from sklearn.neighbors import KNeighborsClassifier
import csv

file_prefix = ".\\data\\"

db = []

#reading the data in a csv file
with open(file_prefix + 'binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

# print(db)

values = {'+':1, '-':2}

predictions = []

for i, instance in enumerate(db):

    X = []
    Y = []

    

    #loop your data to allow each instance to be your test set


    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =

    for j, row in enumerate(db):

        if j != i:
            X.append(list(map(float, row[:2])))
            Y.append(values[row[2]])

    # print(X,Y, end='\n\n')

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = list(map(float, instance[:2]))

    # print(testSample, end='\n\n')

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)



    # print(i, instance)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here

    class_predicted = clf.predict([testSample])[0]
      

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    if (class_predicted == values[instance[2]]):
        predictions.append('Correct Prediction')
    else:
        predictions.append('Wrong Prediction')


#print the error rate
#--> add your Python code here

# print(predictions)

num_of_wrong_predictions = 0
num_of_correct_predictions = 0

for prediction in predictions:
    if prediction == 'Wrong Prediction':
        num_of_wrong_predictions += 1
    else:
        num_of_correct_predictions += 1

print ( "Error Rate: ", str(num_of_wrong_predictions / (num_of_wrong_predictions + num_of_correct_predictions)) )




