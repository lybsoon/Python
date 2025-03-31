## b) funkcyjnie stosując funkcje ale nie wyższego rzędu,

import random
from sys import getsizeof
from datetime import datetime


def splitNumbers(numbers):
    even = []
    odd = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

numbers = random.choices(range(1, 1000001),k=1000000)


time0 = datetime.now()
even, odd = splitNumbers(numbers)
time = (datetime.now() - time0).total_seconds()

print("even: ",even,"odd: ",odd)
print(getsizeof(odd), "bajtow")
print(getsizeof(even), "bajtow")
print("Czas wykonania: ", time, "sekund")