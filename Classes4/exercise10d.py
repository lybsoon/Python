##d) funkcyjnie stosując generator/iterator,

import random
from sys import getsizeof
from datetime import datetime

numbers = random.choices(range(1, 1000001),k=1000000)
time0 = datetime.now()
even = []
odd = []
i = 0
def generator(n):
    for i in n:
        if i % 2 == 0:
            even.append(i)
            yield i

        else:
            odd.append(i)
            yield i



gen = generator(numbers)


for i in range(100):
    print(next(gen))




time = (datetime.now() - time0).total_seconds()

print(getsizeof(odd), "bajtow")
print(getsizeof(even), "bajtow")
print("Czas wykonania: ", time, "sekund")




