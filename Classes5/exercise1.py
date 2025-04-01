## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation

def divisibility(x:int,y:int):
    """
    Fuckcja sprawdza czy liczby z listy sa podzielne
    przez 7 i nie sa wielokrotnosciami 5

    Args:
        x(int): pierwsza watrosc od ktorej sprawdzamy
        y(int): ostatnia wartosc ktora sprawdzamy

    Returns:
        zwraca liczby oddzielone przecinkami które spełniają warunek
    """
    numbers = []
    for i in range(x,y):
        if i % 2 == 0 and i % 5 != 0:
            numbers.append(i)

    return ",".join(map(str,numbers))


print(divisibility.__doc__)
print(divisibility(1000,2101))
