#-------------------------------------------------------------------------
# AUTHOR: Eugene Mondkar
# FILENAME: naive_bayes.py
# SPECIFICATION: complete the naive_bayes.py file with appropriate python code
# FOR: CS 4210- Assignment #2
# TIME SPENT: 20 - 40 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

file_prefix = ".\\data\\"

#reading the training data
#--> add your Python code here

values = {
        "Sunny":1, "Overcast":2, "Rain":3, 
        "Hot":1, "Mild":2, "Cool":3, 
        "High":1, "Normal":2, 
        "Weak":1, "Strong":2,
        "No": 1, "Yes":2
}

db = []

with open(file_prefix + 'weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            entry = []
            for j, element in enumerate(row):
                if j > 0:
                    entry.append(values[element])
            db.append(entry)

    # print(db)

    #transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
    #--> add your Python code here
    # X =

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    X = []
    Y = []

    for row in db:
        X.append(row[:4])
        Y.append(row[4])

    
    #fitting the naive bayes to the data
    clf = GaussianNB()
    clf.fit(X, Y)

    #reading the data in a csv file
    #--> add your Python code here

    test_db = []

    with open(file_prefix + 'weather_test.csv', 'r') as csvfile:
        reader_test = csv.reader(csvfile)
        for i, row in enumerate(reader_test):
            if i > 0: #skipping the header
                test_db.append(row[0:5])

        # print(test_db)

        X_test = []
        Y_predicted = []

        for row in test_db:
            entry = []
            for i, element in enumerate(row):
                if i > 0:
                    entry.append(values[element])
            X_test.append(entry)

        # print(X_test)
        # print(clf.classes_)

        #printing the header os the solution
        print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

        #use your test samples to make probabilistic predictions.
        #--> add your Python code here
        #-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]

        for i, test in enumerate(X_test):
            predicted = clf.predict_proba([test])[0]

            if predicted[0] > predicted[1]:
                test_db[i].append('No')
                test_db[i].append(predicted[0])
            else:
                test_db[i].append('Yes')
                test_db[i].append(predicted[1])
            
            if predicted[0] >= .75 or predicted[1] >= .75:
                print(str(test_db[i][0]).ljust(15) + str(test_db[i][1]).ljust(15) + str(test_db[i][2]).ljust(15) + str(test_db[i][3]).ljust(15) + str(test_db[i][4]).ljust(15) + str(test_db[i][5]).ljust(15) + str(test_db[i][6]).ljust(15))

        
