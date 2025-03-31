##### Task 4
### Utwórz funkcję funcycle(n) która z sekwencji 'INFORMATYKA'
### n krotnie (argument funkcji) wypisze w cyklu każdy z jej elementów
### Wykorzystaj cycle()
import itertools

def funcycle(n):
    i = 0
    for z in itertools.cycle("INFORMATYKA"):
        if i >=n:
            break
        else:
            print(z)
            i+=1

funcycle(22)

