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

def load_truck(truck,package_list,package_hashmap,stop_time=100000000):
    time_delivered_in_seconds = (truck.get_distance() * 200) + truck.get_departure_time()
    if float(time_delivered_in_seconds) <= float(stop_time):
        for package in package_list:
            truck.add_package(package_hashmap.search(package))

def deliver_packages(truck, stop_time=100000000):
    while len(truck.get_packages()) > 0:
        nearest_neighbor.greedy_algorithm_minimize_distance(truck, packageData, addressData, stop_time)

    truck_location = truck.get_location()
    distance = addressData.get_directed_edge(truck_location, 0)
    print('Distance traveling: ', distance)
    truck.set_location(0)
    truck.add_distance(distance)
    print("-------------")
    print(truck.get_distance())
    print("-------------")

def run_distance_calculations(stop_time=100000000):
    load_truck(truck_one, package_group_one, packageData, stop_time)
    deliver_packages(truck_one,stop_time)
    load_truck(truck_two, package_group_two, packageData, stop_time)
    deliver_packages(truck_two,stop_time)
    load_truck(truck_two, package_group_three, packageData, stop_time)
    deliver_packages(truck_two,stop_time)

def rerun_distance_calclations(stop_seconds=100000000):
    read_packages()
    truck_one.clear_distance()
    truck_two.clear_distance()
    run_distance_calculations(stop_seconds)

def print_package_statuses():
    for i in range(packageData.get_size()):
        package = packageData.search(str(i + 1))
        status = package.get_status()
        delivery_time = package.get_time_delivery()
        package_id = package.get_package_id()
        print("Package ID: %s, Status: %s, Delivery Time: %s" % (package_id, status, delivery_time))

def print_intermediate_package_statuses(stop_time):
    for i in range(packageData.get_size()):
        package = packageData.search(str(i + 1))
        status = package.get_status()
        package_id = package.get_package_id()
        print("Package ID: %s, Status: %s, As Of Time: %s" % (package_id, status, stop_time))

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


# Create the hashtable that will hold the package data
packageData = hashtable.ChainingHashTable()

# Create the hashtable that will hold the vertex data
vertexData = hashtable.ChainingHashTable()

# Create the graph that will hold the address data
addressData = graph.Graph()

# Trucks can leave no early than 8:00am which is 28,800 seconds after midnight
# The time the truck leaves, in seconds, is passed in to the constructor.
truck_one = truck.Truck(28800)
truck_two = truck.Truck(28800)

package_group_one = ['1','7','13','14','15','16','19','20','21','27','29','30','34','35','37','39']
package_group_two = ['4','6','11','12','17','18','22','23','24','25','26','28','31','32','36','40']
package_group_three = ['2','3','5','8','9','10','33','38']

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

# Create the two trucks used to deliver the packages
# Since there are only two drivers AND drivers must stay with the same truck while it is in service,
# the third truck cannot be used



# Manually load packages onto the truck, keeping in mind package constraints
# Ensure no more than 16 packages are loaded on each truck
# The following packages are going to the same address and should go on the same truck


# Notes from supplementary requirements
# Packages 13-15, 16, 19, and 20 must go out on the same truck
# Packages 3, 18, 36,and 38 may only go on truck 2
# Packages 3, 25, 28, and 32 cannot leave the hub before 9:05am
read_packages()
run_distance_calculations()
print_package_statuses()

if __name__ == '__main__':
    print("\nWelcome to the Western Governors University Parcel Service (WGUPS) package tracking system. "
          "Please select an option.")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Lookup package statuses")
        print("2. Lookup truck mileage")
        print("3. Rerun distance calculations")
        print("4. Exit the Program")
        option = input("Chose an option (1,2, 3, or 4): ")
        if option == "1":
            user_time = input('Please enter a time (HH:MM:SS)')
            hour, minute, second = map(int, user_time.split(':'))
            lookup_time = datetime.time(hour, minute, second)
            print(lookup_time)
            stop_seconds = int(hour) * 3600 + int(minute) * 60 + int(second)
            rerun_distance_calclations(stop_seconds)
            print_package_statuses()
        elif option == "2":
            rerun_distance_calclations()
            print('Total Distance Truck 1: ', round(truck_one.get_distance(),1))
            print('Total Distance Truck 2: ', round(truck_two.get_distance(),1))
            print('Total Distance All Trucks: ', round((truck_one.get_distance() + truck_two.get_distance()),1))
        elif option == "3":
            truck_one.clear_distance()
            truck_two.clear_distance()
            run_distance_calculations()
            print_package_statuses()
        elif option == "4":
            isExit = False
        else:
            print("Please select a valid number")
