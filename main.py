from Set import Set
from SetFunctions import *

s1 = Set()
s2 = Set()

s1.insert(1)
s1.insert(2)

s2.insert(1)
s2.insert(2)
s2.insert(3)

print(subsetCheck(s1,s2))
print(subsetCheck(s2,s1))
print(generatePowerSet(s2))