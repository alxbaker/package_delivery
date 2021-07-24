import datetime

def greedy_algorithm_minimize_distance(truck, package_data, address_data, stop_time=100000000):
    print('--------')
    print(stop_time)
    print('--------')

    current_vertex = truck.get_location()
    minimum_distance = 100000000
    closest_vertex = -1
    for package in truck.get_packages():
        destination_vertex = package.get_vertex()
        distance = address_data.get_directed_edge(current_vertex, destination_vertex)
        if float(distance) < float(minimum_distance):
            closest_vertex = destination_vertex
            minimum_distance = distance

    # Move the truck to the next address
    truck.set_location(closest_vertex)

    # Add the distance between the current address and the destination address to the distance traveled for this truck
    truck.add_distance(minimum_distance)
    time_delivered_in_seconds = (truck.get_distance() * 200) + truck.get_departure_time()
    print('Distance traveling: ', minimum_distance)

    if float(time_delivered_in_seconds) <= float(stop_time):
        for package in truck.get_packages().copy():
            if package.get_vertex() == closest_vertex:

                time_delivered = datetime.timedelta(seconds=time_delivered_in_seconds)
                package.set_time_delivered(time_delivered)
                package.set_status('delivered')
                truck.remove_package(package)

                print("Delivery Time:", time_delivered)
    else:
        truck.clear_packages()