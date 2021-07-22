# Name: Alex Baker, Student ID: 000998897
# C950 Data Structures and Algorithms II
# Performance Assessment NHP2

# Import modules and classes required to run the main program
import csv
import hashtable
import package
import vertex
import graph
import truck
import greedy

# Create the hashtable that will hold the package data
packageData = hashtable.ChainingHashTable()

# Create the hashtable that will hold the vertex data
vertexData = hashtable.ChainingHashTable()

# Create the graph that will hold the address data
addressData = graph.Graph()

# Read the vertex data from the csv file
with open('vertex_names.csv') as vertexList:
    readCSV = csv.reader(vertexList, delimiter=',')

    # Loop through each row in the csv file, instantiating variables with file values
    for iteration, row in enumerate(readCSV):
        index = iteration
        label = row[0]
        address = row[1]

        # Create a vertex object using file values
        currentVertex = vertex.Vertex(index, label, address)

        # Add the vertex object to the vertex hash table
        vertexData.insert(address, currentVertex)

        # Add the vertex object to the graph
        addressData.add_vertex(index)

# Read the distance data from the csv file
with open('distances.csv') as distanceList:
    readCSV = csv.reader(distanceList, delimiter=',')

    # Loop through each row in the csv file, keeping track of the index number for the vertex as fromVertex
    for fromVertex, row in enumerate(readCSV):

        # Loop through the values within each row, keeping track of the index number for the destination vertex as toVertex
        for toVertex, distanceValue in enumerate(row):

            # Add the distance between the toVertex and the fromVertex to the graph as an undirected edge
            addressData.add_undirected_edge(fromVertex, toVertex, distanceValue)

    # Read the distance data from the csv file
    with open('distances.csv') as distanceList:
        readCSV = csv.reader(distanceList, delimiter=',')

        # Loop through each row in the csv file, keeping track of the index number for the vertex as fromVertex
        for fromVertex, row in enumerate(readCSV):

            # Loop through the values within each row, keeping track of the index number for the destination vertex as toVertex
            for toVertex, distanceValue in enumerate(row):
                # Add the distance between the toVertex and the fromVertex to the graph as an undirected edge
                addressData.add_undirected_edge(fromVertex, toVertex, distanceValue)

# Read the package data from the csv file
with open('packages.csv') as packageList:
    readCSV = csv.reader(packageList, delimiter=',')

    # Loop through each row in the csv file, instantiating variables with file values
    for row in readCSV:
        packageID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipCode = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]

        # Create a package object using file values
        currentPackage = package.Package(packageID, address, city, state, zipCode, deadline, weight, notes)

        # Add the package object to the hash table, using the package ID as the key
        packageData.insert(packageID, currentPackage)

        # Add the vertex number to the package object
        currentPackage.set_vertex(vertexData)



# Create the three trucks used to deliver the packages
truck_one = truck.Truck(28800)
truck_two = truck.Truck(28800)
truck_three = truck.Truck(28800)

# Manually load packages onto the truck, keeping in mind package constraints
# The following packages are going to the same address and should go on the same truck
# 20 and 21, 10:30 / 13 and 39, 10:30 / 15, 16, and 34, 9:00 / 19. EOD
# 4 and 40, 10:30
# 7 and 29, 10:30
# 25 and 26, 10:30
# 31 and 32, 10:30 (can't leave before 9:05)
# 8 and 30, 10:30 (9 has the same address but will not be updated until 10:20)
# 5, 37, and 38, 10:30 (truck 2)
# 27 and 35, EOD
# 2 and 33, EOD


truck_one.add_package(packageData.search('1'))
truck_one.add_package(packageData.search('2'))
truck_one.add_package(packageData.search('3'))
truck_one.add_package(packageData.search('4'))
truck_one.add_package(packageData.search('5'))
truck_one.add_package(packageData.search('6'))
truck_one.add_package(packageData.search('7'))

while len(truck_one.get_packages()) > 0:
    greedy.greedy_algorithm_minimize_distance(truck_one, packageData, addressData)

    print('The following packages are now on the truck:')
    for package in truck_one.get_packages():
        print(package)

    print('The truck has now traveled the following number of miles')
    print(truck_one.get_distance())

print(packageData.search('1'))
print(packageData.search('2'))
print(packageData.search('3'))
print(packageData.search('4'))
print(packageData.search('5'))
print(packageData.search('6'))
print(packageData.search('7'))


if __name__ == '__main__':
    print("\nWelcome to C950: Classic Movies: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get Movie Data")
        print("2. Run Greedy Algorithm with a Budget")
        print("3. Run Dijkstra Algorithm")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")
        if option == "1":
            print('You selected option 1')
        elif option == "2":
            print('You selected option 2')
        elif option == "3":
            print('You selected option 3')
        elif option == "4":
            isExit = False
        else:
            print("Please select a valid number")
