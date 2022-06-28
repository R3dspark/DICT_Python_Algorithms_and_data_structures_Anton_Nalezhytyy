from Praktik3.RAM import RAM


class Node:

    def __init__(self, data: RAM):
        self.data = data    # type: RAM
        self.next = None    # type: [Node, None]

    def has_value(self, value: RAM):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
