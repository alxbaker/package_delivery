# Package class
class Package:
    def __init__(self, packageID, address, city, state, zipCode, deadline, weight, notes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

        # Set the vertex for all new packages to a vertex that does not exist
        self.vertex = -1

        # Set the status for all new packages as at the hub
        self.status = 'at the hub'

        # Set the delivery time for all new packages as an empty string
        self.timeDelivered = ''

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.packageID, self.address, self.city, self.state, self.zipCode, self.deadline, self.weight, self.notes, self.status, self.timeDelivered, self.vertex)

    # This function returns a package's address
    def get_address(self):
        return self.address

    # This function sets a package's vertex
    def set_vertex(self, vertex_data):
        address = self.get_address()
        vertex = vertex_data.search(address)
        index = vertex.get_index()
        self.vertex = index

    # This function sets a package's delivery time
    def set_time_delivered(self, time_delivered):
        self.timeDelivered = time_delivered

    # This function gets a package's delivery time
    def get_time_delivery(self):
        return self.timeDelivered

    # This function gets a package's delivery ID
    def get_package_id(self):
        return self.packageID

    # This function sets a package's status
    def set_status(self, status):
        self.status = status

    # This function gets a package's delivery vertex
    def get_vertex(self):
        return self.vertex

    # This function gets a package's delivery status
    def get_status(self):
        return self.status