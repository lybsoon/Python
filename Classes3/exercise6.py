import sil

number1 = int(input("podaj pierwsza liczbe: "))
number2 = int(input("podaj druga liczbe: "))

def Newton(n,k):
    result = sil.silnia(n) / (sil.silnia(k) * sil.silnia(n-k))
    print(result)

Newton(number1,number2)