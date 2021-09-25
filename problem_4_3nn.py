import csv

def calculateDistance(p1, p2):
    distance = 0
    for coord in range(len(p1)):
        distance += (( p1[coord] - p2[coord] ) ** 2)

    return (distance ** 0.5)

def sortByDistance(distances):
    distances.sort(key = lambda x: x[1])

def nearestNeighbor(distances, k):
    nearest_neighbors = []

    for i in range(k):
        nearest_neighbors.append(distances[i])

    return nearest_neighbors


def prediction(distances, k):
    
    sortByDistance(distances)

    nearest_neighbors = nearestNeighbor(distances, k)

    # print(nearest_neighbors)

    count_1 = 0
    count_2 = 0
    count_3 = 0
    most_frequent_class = None

    for neighbor in nearest_neighbors:
        if neighbor[0][3] == 1:
            count_1 += 1
        elif neighbor[0][3] == 2:
            count_2 += 1
        elif neighbor[0][3] == 3:
            count_3 += 1
    
    max = count_2
    most_frequent_class = 2
    if count_1 > max:
        most_frequent_class = 1
    if count_3 > max:
        most_frequent_class = 3
    
    # print(point[2])
    # print(most_frequent_class)

    return most_frequent_class

if __name__ == "__main__":

    test_sample = [154, 205, 50]

    k = 3

    with open('./data/problem_4_training_3nn.csv') as csv_points:
        points_reader = csv.reader(csv_points, delimiter=',')

        points = []

        for entry in points_reader:
            # print(entry)
            points.append(list(map(int, entry)))

        # print(points)

        distances = []

        for i, instance in enumerate(points):
            
            distance = calculateDistance(instance[:3],test_sample)
            distances.append([instance, distance])

            print('Distance between point 10 and point {} is: {}'.format(i+1, distance))

        
        # print('\n\n', distances, end='\n\n')

        print('Predicted Class: ', prediction(distances,k))

        # print(nearest_neighbors)
