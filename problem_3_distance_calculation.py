import csv

def calculateDistance(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return ((((x2 - x1 ) ** 2) + ((y2 - y1)**2) ) ** 0.5)

def sortByDistance(distances):
    distances.sort(key = lambda x: x[1])

def nearestNeighbor(distances, k):
    nearest_neighbors = []

    for i in range(k):
        nearest_neighbors.append(distances[i])

    return nearest_neighbors

def determinePrediction(point, distances, k):
    nearest_neighbors = nearestNeighbor(distances, k)

    # print(nearest_neighbors)

    count_plus = 0
    count_minus = 0
    most_frequent_class = None

    for neighbor in nearest_neighbors:
        if neighbor[0][2] == '+':
            count_plus += 1
        elif neighbor[0][2] == '-':
            count_minus += 1
    
    if count_plus >= count_minus:
        most_frequent_class = '+'
    else:
        most_frequent_class = '-'
    
    # print(point[2])
    # print(most_frequent_class)

    if point[2] == most_frequent_class:
        return 'Correct Prediction'
    else:
        return 'Wrong Prediction'



if __name__ == "__main__":

    k = 1

    with open('./data/binary_points.csv') as csv_binary_points:
        binary_points_reader = csv.reader(csv_binary_points, delimiter=',')
        next(binary_points_reader)

        points = []

        for entry in binary_points_reader:
            # print(entry)
            element = list(map(int, entry[:2]))
            element.append(entry[2])
            points.append(element)

        print(points)

        predictions = []

        for i in range(len(points)):

            distances = []

            # nearest_neighbor = [None,99999]
            p1 = points[i]
            
            print('-------- For', p1, '--------')

            for j in range(len(points)):
                if i != j:
                    p2 = points[j]
                    distance = calculateDistance(p1[:2], p2[:2])
                    print(distance)
                    distances.append([p2, distance])
                    # if distance < nearest_neighbor[1]:
                    #     nearest_neighbor[0] = p2
                    #     nearest_neighbor[1] = distance
            
            # print('nearest neighbor', nearest_neighbor)

            # if p1[2] == nearest_neighbor[0][2]:
            #     print('Correct Prediction')
            # else:
            #     print('Wrong Prediction')

            # print(distances, end='\n\n')
            sortByDistance(distances)
            # print(distances)

            result = determinePrediction(p1, distances, k)

            predictions.append(result)

            print(result)

            print('---------------------------------')

        num_of_wrong_predictions = 0
        num_of_correct_predictions = 0
        # print(predictions)

        for prediction in predictions:
            if prediction == 'Wrong Prediction':
                num_of_wrong_predictions += 1
            else:
                num_of_correct_predictions += 1

        print ( "Error Rate: ", str(num_of_wrong_predictions / (num_of_wrong_predictions + num_of_correct_predictions)) )