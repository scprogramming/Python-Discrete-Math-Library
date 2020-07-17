import math
from Set import Set

def subsetCheck(set1,set2):
    isSubset = True
    i = 0

    items = set1.getItems()

    while i < len(items) and isSubset:
        if items[i] not in set2:
            isSubset = False
        i += 1

    return isSubset

def generatePowerSet(set):
    powers = Set()
    total = int(math.pow(2,len(set)))
    keys = set.getItems()

    for i in range(0,total):
        tempSet = []
        binRep = bin(i)[2:]

        while len(binRep) < len(set):
            binRep = '0' + binRep

        j = 0
        for c in binRep:
            if c == '1':
                tempSet.insert(0,keys[j])
            j += 1
        powers.insert(tuple(tempSet))

    return powers
