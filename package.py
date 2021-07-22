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
        self.vertex = -1

        # Set the status for all new packages as at the hub
        self.status = 'at the hub'

        # Set the delivery time for all new packages as an empty string
        self.timeDelivered = ''

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.packageID, self.address, self.city, self.state, self.zipCode, self.deadline, self.weight, self.notes, self.status, self.timeDelivered, self.vertex)

    def get_address(self):
        return self.address

    def get_id(self):
        return self.packageID

    def set_vertex(self, vertex_data):
        address = self.get_address()
        vertex = vertex_data.search(address)
        index = vertex.get_index()
        self.vertex = index

    def set_time_delivered(self, time_delivered):
        self.timeDelivered = time_delivered

    def get_time_delivery(self):
        return self.timeDelivered

    def set_status(self, status):
        self.status = status

    def get_vertex(self):
        return self.vertex