class Truck:
    def __init__(self, departure_time):
        self.distance = 0

        # Truck objects can conain a set of packages
        self.packages = set()
        self.location = 0

        # Departure time will be tracked in seconds
        self.departure_time = departure_time

    def __str__(self):
        return "%s, %s, %s" % (self.distance, self.packages, self.location,)

    # This function is used to add packages to the truck and set the status as en route
    def add_package(self, package_object):
        self.packages.add(package_object)
        package_object.set_status('en route')

    # This function is used to remove packages from the truck
    def remove_package(self, package_object):
        self.packages.remove(package_object)

    # This function is used to retrieve the set of packages on the truck
    def get_packages(self):
        return self.packages

    # This function is used to reset truck distance
    def clear_distance(self):
        self.distance = 0

    # This function is used to remove all packages from the truck
    def clear_packages(self):
        self.packages.clear()

    # This function is used to add to the truck's distance traveled
    def add_distance(self, distance):
        self.distance += float(distance)

    # This function is used to retrieve the total distance the truck has traveled
    def get_distance(self):
        return self.distance

    # This function is used to return the index number of the truck's current vertex
    def get_location(self):
        return self.location

    # This function is used to move the truck to a specific vertex
    def set_location(self, location):
        self.location = location

    # This function returns the truck's departure time in seconds
    def get_departure_time(self):
        return self.departure_time
