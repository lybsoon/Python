#### Task 9
## Utwórz generator dla ciągu Fibonacciego (pierwszy wyraz ciągu jest równy 0, drugi jest równy 1,
## a każdy kolejny element ciągu jest sumą dwóch poprzednich. Wypisz n-ty element tego ciągu
## Użytkownik deklaruje ilość elementów (n).
## Specyfikacja: użyj accumulate() lub reduce() do wygenerowania ciągu Fibonacciego
from functools import reduce

def fib(n):
    if n == 0:
        yield 0
        return

    fibonacci = reduce(lambda x, _: x + [x[-1] + x[-2]],range(n-1),[0,1])

    yield fibonacci[n-1]

t = int(input("Podaj n ty wyraz ciagu fibonaciego: "))
generator = fib(t)

print(next(generator))


 