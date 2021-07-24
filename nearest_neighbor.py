import datetime

# This function finds the nearest neighbor to the current vertex.
# It accepts a truck object, the address hash table, and a stop time
# The stop time is used to stop delivery packages when looking up package statuses as of a specific time
# Space time complexity is O(n) as there is only one loop at a time. They are not nested
def greedy_algorithm_minimize_distance(truck, address_data, stop_time=100000000):

    # Get the truck's current location
    current_vertex = truck.get_location()

    # Set the minimum distnace to a high number
    minimum_distance = 100000000

    # Set the vertex to an index that doesn't exist
    closest_vertex = -1

    # Iterate through the packages in the truck
    for package in truck.get_packages():

        # Get the packages vertex
        destination_vertex = package.get_vertex()

        # Determine the distance between the packages vertex and the truck's current vertex
        distance = address_data.get_directed_edge(current_vertex, destination_vertex)

        # If the distance is less than the minimum_distance
        if float(distance) < float(minimum_distance):
            # Set the closest_vertex to the package's vertex
            closest_vertex = destination_vertex

            # Set the minimum_distance to the distance between the truck's current location and the package's vertex
            minimum_distance = distance

    # Move the truck to the closest vertex
    truck.set_location(closest_vertex)

    # Add the distance between the current address and the destination address to the distance traveled for this truck
    truck.add_distance(minimum_distance)

    # Calculate the packages delivery time in seconds
    time_delivered_in_seconds = (truck.get_distance() * 200) + truck.get_departure_time()

    # If the delivery time is less than or equal to the stop time...
    if float(time_delivered_in_seconds) <= float(stop_time):
        # Format the time delivered in seconds to a readable time
        time_delivered = datetime.timedelta(seconds=time_delivered_in_seconds)

        # Iterate through all the packages on the truck
        for package in truck.get_packages().copy():

            # If the package's vertex number matches the truck's current vertex...
            if package.get_vertex() == closest_vertex:

                # Set the package's delivery time
                package.set_time_delivered(time_delivered)

                # Set the package's status to delivered
                package.set_status('delivered')

                # Remove the package from the truck
                truck.remove_package(package)

    # If the delivery time is greater than the stop_time, remove all packages from the truck
    else:
        truck.clear_packages()
