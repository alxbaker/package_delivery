# The vertex class creates vertex objects that hold an index, label, and address
# This data is used to match packages to a specific vertex number
class Vertex:
    def __init__(self, index, label, address):
        self.index = index
        self.label = label
        self.address = address

    def __str__(self):
        return "%s, %s, %s" % (self.index, self.label, self.address,)

    def get_index(self):
        return self.index

