## Porównaj czas obliczeń i ilość zajmowanej pamięci przez dane w przypadku gdy programujesz
## a) imperatywnie/sturkturalnie,
import random
from sys import getsizeof
from datetime import datetime

even = []
odd = []
numbers = random.choices(range(1, 1000001),k=1000000)
time0 = datetime.now()

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even: ",even,"odd: ",odd)

time = (datetime.now() - time0).total_seconds()
print(getsizeof(odd), "bajtow")
print(getsizeof(even), "bajtow")
print("Czas wykonania: ", time, "sekund")


