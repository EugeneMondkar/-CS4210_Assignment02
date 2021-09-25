import csv


def decisionTree(entry):

    result = None
    
    if entry[3].strip() == 'Normal': # Tear determination

        if entry[1].strip() == 'Myope': # Spectacle determination
            result = 'Yes'
        
        elif entry[1].strip() == 'Hypermetrope': # Spectacle determination
            
            if entry[2].strip() == 'Yes': # Astigmatism determination
                result = 'No'

            elif entry[2].strip() == 'No': # Astigmatism determination
                result = 'Yes'
    
    elif entry[3].strip() == 'Reduced': # Tear determination
        result = 'No'

    return result

def confusionMatrix(actual_class, predicted_class):
    result = None

    if actual_class == 'Yes' and predicted_class == 'Yes':
        result = 'True Positive'
    elif actual_class == 'Yes' and predicted_class == 'No':
        result = 'False Negative'
    elif actual_class == 'No' and predicted_class == 'Yes':
        result = 'False Positive'
    elif actual_class == 'No' and predicted_class == 'No':
        result = 'True Negative'

    return result

def performanceCounter(accuracy_tracker):
    num_TP = 0
    num_FP = 0
    num_FN = 0
    num_TN = 0

    for accuracy in accuracy_tracker:
        if accuracy == 'True Positive':
            num_TP += 1
        elif accuracy == 'False Negative':
            num_FN += 1
        elif accuracy == 'False Positive':
            num_FP += 1
        elif accuracy == 'True Negative':
            num_TN += 1

    return num_TP, num_FP, num_FN, num_TN


def calculatePrecision(accuracy_tracker):
    
    count = performanceCounter(accuracy_tracker)

    num_TP = count[0]
    num_FP = count[1]

    return num_TP / (num_TP + num_FP)

def calculateRecall(accuracy_tracker):

    count = performanceCounter(accuracy_tracker)

    num_TP = count[0]
    num_FN = count[2]

    return num_TP / (num_TP + num_FN)

def calculateF1(accuracy_tracker):
    recall = calculateRecall(accuracy_tracker)
    precision = calculatePrecision(accuracy_tracker)

    return (2 * recall * precision) / (recall + precision)


if __name__ == "__main__":
    
    accuracy_tracker = []

    with open('./data/contact_lens_test_problem_1.csv') as csv_contact_lens_test:
        contact_lens_reader = csv.reader(csv_contact_lens_test, delimiter=',')
        next(contact_lens_reader) # discard header
        
        for entry in contact_lens_reader:
            # predicted_result = decisionTree(entry[:4])
            print(entry[:4], end='\n\t --> ')
            predicted_result = decisionTree(entry[:4])
            print('Actual Result: ', entry[4].strip(), '| Predicted Result: ', predicted_result, end=' | ')
            accuracy = confusionMatrix(entry[4].strip(), predicted_result)
            accuracy_tracker.append(accuracy)
            print('Accuracy:', accuracy)

        print("\nCollected results: \n")
        count = 1
        for i in range(len(accuracy_tracker)):
            print(accuracy_tracker[i], end='\t')
            if count % 2 == 0:
                print()
            count += 1
        count = performanceCounter(accuracy_tracker)
        print("\nNumber of True Positives =", count[0])
        print("Number of False Positives =", count[1])
        print("Number of True Negatives =", count[3])
        print("Number of False Negatives =", count[2])
        print("Precision:", calculatePrecision(accuracy_tracker))
        print("recall:", calculateRecall(accuracy_tracker))
        print("F1-Measure:", calculateF1(accuracy_tracker))

