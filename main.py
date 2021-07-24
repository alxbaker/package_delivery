# Name: Alexander Baker, Student ID: 000998897
# C950 Data Structures and Algorithms II
# Performance Assessment NHP2
# Please see the Word document included with this project for narrative descriptions to satisfy remaining requirements

# Import modules and classes required to run the main program
import csv
import datetime
import hashtable
import package
import vertex
import graph
import truck
import nearest_neighbor

# Define functions that will run more than once and can be triggered by user actions

# This function accepts a truck object, a list of packages, and a package hashtable object
# It is used to load the packages onto a specific truck
# The stop time is used to stop iterating over the package list, when looking up packages as of a specific time
# Space time complexity is O(n) as there is one loop
def load_truck(truck, package_list, package_hashmap, stop_time=100000000):
    time_traveled = (truck.get_distance() * 200) + truck.get_departure_time()
    if float(time_traveled) <= float(stop_time):
        for package in package_list:
            truck.add_package(package_hashmap.search(package))

# This function accepts a truck object and is use to deliver the packages on a specific truck
# The stop time is used to stop delivery packages when looking up package statuses as of a specific time
# Space time complexity is O(n) as there is a one loop
def deliver_packages(truck, stop_time=100000000):
    # Continue delivering packages as long as there are packages on the truck
    while len(truck.get_packages()) > 0:

        # User the algorithm in nearest_neighbor.py, intended to minimize distance.
        # See nearest_neighbor.py for a description of this function
        nearest_neighbor.greedy_algorithm_minimize_distance(truck, addressData, stop_time)

    # After all packages have been delivered, determine the distance to return the truck to the hub (vertex 0)
    # Get the trucks current location
    truck_location = truck.get_location()

    # Calculate the distance between the current location and the hub
    distance = addressData.get_directed_edge(truck_location, 0)

    # Move the truck back to the hub
    truck.set_location(0)

    # Add the distance back to the hub to the total distance traveled
    truck.add_distance(distance)

# This function is used when running distance calculations
# The stop time is used to stop delivery packages and loading trucks when looking up statuses as of a specific time
# Space time complexity has been defined for individual functions included within this function
def run_distance_calculations(stop_time=100000000):
    # Read package data
    read_packages()

    # Clear any truck distances
    truck_one.clear_distance()
    truck_two.clear_distance()

    # Load and delivery packages
    load_truck(truck_one, package_group_one, packageData, stop_time)
    deliver_packages(truck_one,stop_time)
    load_truck(truck_two, package_group_two, packageData, stop_time)
    deliver_packages(truck_two,stop_time)
    load_truck(truck_two, package_group_three, packageData, stop_time)
    deliver_packages(truck_two,stop_time)

# This function is used to print the package statuses, including package ID, status, and delivery time
# Space time complexity is O(n) as there is a one loop
def print_package_statuses():

    # Iterate through packages in the hash table
    for i in range(packageData.get_size()):
        package = packageData.search(str(i + 1))
        status = package.get_status()
        delivery_time = package.get_time_delivery()
        package_id = package.get_package_id()
        print("Package ID: %s, Status: %s, Delivery Time: %s" % (package_id, status, delivery_time))

# This function loads packages from the csv file to the hash table
# Space time complexity is O(n) as there is a one loop
def read_packages():

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

            # Add the vertex number to the package object
            currentPackage.set_vertex(vertexData)

            # Add the package object to the hash table, using the package ID as the key
            packageData.insert(packageID, currentPackage)

# Create objects used to hold data

# Create the hashtable that will hold the package data
packageData = hashtable.ChainingHashTable()

# Create the hashtable that will hold the vertex data
vertexData = hashtable.ChainingHashTable()

# Create the graph that will hold the address data
addressData = graph.Graph()

# Create the truck objects that will hold packages and distances.
# The time the truck leaves, in seconds, is passed in to the constructor.
# Truck one will leave at 8:00am which is 28,800 seconds after midnight
# Truck two will leave at 9:05am which is 32700 seconds
truck_one = truck.Truck(28800)
truck_two = truck.Truck(32700)

# Create package groupings
# Only 16 packages can be on the truck at one time
package_group_one = ['1', '7', '13', '14', '15', '16', '19', '20', '21', '27', '29', '30', '34', '35', '37', '39']
package_group_two = ['4', '6', '11', '12', '17', '18', '22', '23', '24', '25', '26', '28', '31', '32', '36', '40']
package_group_three = ['2', '3', '5', '8', '9', '10', '33', '38']

# Read the vertex data from the csv file
# Space time complexity is O(n) as there is a one loop
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
# Space time complexity is O(n^2) as there is are two loops
with open('distances.csv') as distanceList:
    readCSV = csv.reader(distanceList, delimiter=',')

    # Loop through each row in the csv file, keeping track of the index number for the vertex as fromVertex
    for fromVertex, row in enumerate(readCSV):

        # Loop through the values within each row, keeping track of the index number for the destination vertex as toVertex
        for toVertex, distanceValue in enumerate(row):

            # Add the distance between the toVertex and the fromVertex to the graph as an undirected edge
            addressData.add_undirected_edge(fromVertex, toVertex, distanceValue)


if __name__ == '__main__':
    print("\nWelcome to the Western Governors University Parcel Service (WGUPS) package tracking system. "
          "Please select an option.")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Run distance calculations")
        print("2. Print truck mileage")
        print("3. Print package statuses as of a specific time")
        print("4. Exit the Program")
        option = input("Chose an option (1,2, 3, or 4): ")

        if option == "1":
            run_distance_calculations()
            print_package_statuses()
        elif option == "2":
            run_distance_calculations()
            print('Total Distance Truck 1: ', round(truck_one.get_distance(), 1))
            print('Total Distance Truck 2: ', round(truck_two.get_distance(), 1))
            print('Total Distance All Trucks: ', round((truck_one.get_distance() + truck_two.get_distance()), 1))
        elif option == "3":
            user_time = input('Enter a time after 08:00:00 in military time (HH:MM:SS) to check package statuses')
            hour, minute, second = map(int, user_time.split(':'))
            lookup_time = datetime.time(hour, minute, second)
            stop_seconds = int(hour) * 3600 + int(minute) * 60 + int(second)
            stop_time = datetime.timedelta(seconds=stop_seconds)
            print('Printing package statuses as of %s' % (stop_time))
            run_distance_calculations(stop_seconds)
            print_package_statuses()
        elif option == "4":
            isExit = False
        else:
            print("Please select a valid number")
