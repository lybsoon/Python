### Task 7
## początkowa kwota na 3mc lokacie to k = 10000, oprocentowanie lokaty to 0.01%
## oblicz jaką kwotę zgromadzi użytkownik po upływie t = 9mc
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego
from itertools import accumulate
from types import LambdaType


def deposite(k, months , rate):

    rates = [rate] * months
    accumulated = list(accumulate(rates, initial=k, func = lambda x,y: x+x *y))
    return accumulated[-1]


k = 10000
rate = 0.0001
months = 9

result = round(deposite(k,months,rate),2)

print(result)
