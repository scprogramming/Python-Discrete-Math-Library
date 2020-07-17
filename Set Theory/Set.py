class Set:
    #initalization
    def __init__(self):
        self.values = dict()

    #Insert a value into the set
    def insert(self,value):
        if value not in self.values.keys():
            self.values[value] = value

    #Remove a value from the set
    def remove(self,value):
        del self.values[value]

    #Print the contents of the set
    def __str__(self):
        contents = "{"
        i =0
        for keys in self.values.keys():
            if i == 0:
                contents += str(keys)
            else:
                contents += "," + str(keys)
            i += 1
        contents += "}"
        return contents

    #iterate the set
    def __iter__(self):
        return iter(self.values.copy())

    #determine the size of the set
    def __len__(self):
        return len(self.values)

    #Check for equality of two sets
    def __eq__(self, other):
        return other.getValues == self.values

    #Check if an element is in the set
    def __contains__(self, item):
        return item in self.values.keys()

    #Check if list is empty
    def isEmpty(self):
        return len(self.values) == 0

    #Get all of the items in the set
    def getItems(self):
        return list(self.values.keys())
