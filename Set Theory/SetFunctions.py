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

def generateCartesianProduct(set1,set2):
    productList = Set()
    for a in set1.getItems():
        for b in set2.getItems():
            item = [a,b]
            productList.insert(tuple(item))
    return productList

def union(set1,set2):
    unionSet = Set()

    for x in set1:
        unionSet.insert(x)
    for x in set2:
        unionSet.insert(x)

    return unionSet

def intersect(set1,set2):
    intersectSet = Set()

    for x in set1:
        if x in set2:
            intersectSet.insert(x)

    return intersectSet

def setDifference(set1,set2):
    differenceSet = Set()

    for x in set1:
        if x not in set2:
            differenceSet.insert(x)

    return differenceSet