### Task 8
## Utwórz listę 100 losowych liczby
## utwórz podzbiór liczb parzystych większych od 10
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego
import random

list1 = random.choices(range(1,101), k = 100)

resultLambda = filter(lambda x: x>10,list1)

for i, number in enumerate(resultLambda):
    print(f"insex:{i + 1} , Wartość:{number}")

