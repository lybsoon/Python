### Task 8
### Utwórz własny generator liczb które są kolejnymi wielokrotnosciami liczby cztery tj. 4,16,32,64,... itd
### n - liczbę elementów w generatorze deklaruje użytkownik
### np. dla n=3,  funkcja next w kolejnych wywołaniach zwraca:  4, 16, 32



def powerOf4():
    i = 1
    while True:
        yield 4 ** i
        i += 1



n = int(input("Podaj ile wielokrotnosci 4 wygenerować: "))
generator = powerOf4()

for i in range(n):
    print(next(generator))





