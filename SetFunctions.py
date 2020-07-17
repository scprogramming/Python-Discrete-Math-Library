def subsetCheck(set1,set2):
    isSubset = True

    for element in set1:
        if element not in set2:
            isSubset = False

    return isSubset