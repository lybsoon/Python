## c) funkcyjnie stosując funkcje wyższego rzędu, do zrównoleglenia obliczeń

import random
from sys import getsizeof
from datetime import datetime


numbers = random.choices(range(1, 1000001),k=1000000)
time0 = datetime.now()

even = list(filter(lambda x: x % 2 == 0,numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))


time = (datetime.now() - time0).total_seconds()

print("even: ",even,"odd: ",odd)
print(getsizeof(odd), "bajtow")
print(getsizeof(even), "bajtow")
print("Czas wykonania: ", time, "sekund")