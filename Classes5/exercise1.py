## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation
import pickle

def divisibility(x:int,y:int):
    """
    Fuckcja sprawdza czy liczby z listy sa podzielne
    przez 7 i nie sa wielokrotnosciami 5, z obsluga bledow

    Args:
        x(int): pierwsza watrosc od ktorej sprawdzamy
        y(int): ostatnia wartosc ktora sprawdzamy

    Returns:
        zwraca liczby oddzielone przecinkami które spełniają warunek
    """
    try:
        if x>y:
            raise ValueError("wartosc poczotkowa nie moze byc wieksza od ostaniej")


        numbers = []
        for i in range(x,y):
            if i % 2 == 0 and i % 5 != 0:
                numbers.append(i)

        return numbers

    except (ValueError) as e:
        print("blad:",e)
        return []


result = divisibility(1000,2101)
with open("test.txt","wb") as file:
    pickle.dump(result,file)

print(",".join(map(str,result)))
print(divisibility.__doc__)

