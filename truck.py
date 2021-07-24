class Truck:
    def __init__(self, departure_time):
        self.distance = 0
        self.packages = set()
        self.location = 0

        #departure time will be tracked in seconds
        self.departure_time = departure_time

    def __str__(self):
        return "%s, %s, %s" % (self.distance, self.packages, self.location,)

    def add_package(self, package_object):
        self.packages.add(package_object)
        package_object.set_status('en route')

    def remove_package(self, package_object):
        self.packages.remove(package_object)

    def get_packages(self):
        return self.packages

    def clear_distance(self):
        self.distance = 0

    def clear_packages(self):
        self.packages.clear()

    def add_distance(self, distance):
        self.distance += float(distance)

    def get_distance(self):
        return self.distance

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_departure_time(self):
        return self.departure_time
