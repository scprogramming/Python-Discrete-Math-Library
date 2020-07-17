class Set:

    def __init__(self):
        self.values = dict()

    def insert(self,value):
        if value not in self.values.keys():
            self.values[value] = value

    def remove(self,value):
        del self.values[value]

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

    def __iter__(self):
        return iter(self.values.copy())

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        return other.getValues == self.values

    def isEmpty(self):
        return len(self.values) == 0

    def __contains__(self, item):
        return item in self.values.keys()

    def getItems(self):
        return list(self.values.keys())
