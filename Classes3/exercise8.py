# ########################## Task 8
#### Write a script, using reduce(), which will multiply elements in range (1, 100)

import functools

numbers = list(range(1,100))

resultLambda = lambda x,y : x*y
resultReduce = functools.reduce(resultLambda,numbers)

print(resultReduce)