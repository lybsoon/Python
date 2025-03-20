################################## Task 12
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.
import random

randomNumbers = random.sample(range(100),100)

oddNumbers = []

for i in randomNumbers:
    if i % 2 !=0:
        oddNumbers.append(i)


oddNumbers.sort()
print(oddNumbers)