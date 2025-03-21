# ########################## Task 9
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
### use filter

numbers = list(range(2000,3201))

resultLambda = filter(lambda x: x % 5 !=0 and x % 7 ==0, numbers)

print(",".join(map(str,resultLambda)))
