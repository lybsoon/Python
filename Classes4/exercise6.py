### Task 6
### Posiadasz grupę N-studentów (N-indeksów), podziel w/w grupę na n-podgrup
### Specyfikacja kodu: funkcja, wykorzystanie iteratora kombinatorycznego
from itertools import combinations


students = list(range(1,10))

n = int(input("ile osobowe grupy mam stowrzyć: "))

print(list(combinations(students,n)))