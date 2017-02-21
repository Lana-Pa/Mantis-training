from sys import maxsize

class Project:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


    def __repr__(self):
        return "PROJECT:%s;%s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name

    def max(self):
       return maxsize