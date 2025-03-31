##### Task 2
### Utwórz listę zawierającą 10000 losowych liczb
### wyselekcjonuj liczby mniejsze niż 3 i parzyste
### Wykorzystaj filter() i funkcje z modułu operators

import random
import operator


list1 = random.choices(range(0,10000), k=10000)

resultLambda1 = filter(lambda x: operator.mod(x,2) == 0 or x<3,list1)

print(list(resultLambda1))