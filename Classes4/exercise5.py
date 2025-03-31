##### Task 5
### Oblicz iloczyn kartezjański 3D, [1,2,3], ['a','b','c'], [True,False]
from itertools import product

list1 = [1,2,3]
list2 = ["a","b","c"]
list3 = [True, False]

print(list(product(list1,list2,list3)))