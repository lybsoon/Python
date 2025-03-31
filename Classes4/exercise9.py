### Task 9
## a) Utwórz własny generator zwracający 1000 losowych liczb parzystych z zakresu 0-100000000
import random

list1 = random.sample(range(0,100000000),1000)

def randomNumbers():
    for i in list1:
        yield i

generator = randomNumbers()

for i in range(10):
    print(next(generator))

