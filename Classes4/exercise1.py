##### Task 1
### Utwórz 2 listy, pierwsza liczby od 1 do 100, druga 100 losowych liczb
### odejmnij wartości elementów listy pierwszej od drugiej
### Wykorzystaj map() i funkcję sub() z modułu operators
import operator
import random

lista1 = list(range(1,101))
lista2 = random.sample(range(1,101),100)

print(list(map(operator.sub,lista1,lista2)))