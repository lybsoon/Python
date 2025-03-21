# ########################## Task 7
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.


numbers = list(range(1,100))

resultLambda = filter(lambda x: x % 2 == 0, numbers)

print(",".join(map(str, resultLambda)))