class Node(object):
    def __init__(self, position, parent = None):
        self.position = position
        self.parent = parent
        self.f = self.g = self.h = 0
    
    def __eq__(self, other):
        return self.position == other.position