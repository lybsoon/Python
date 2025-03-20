####Task 10
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).


for i in range(1,100):
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))
    if x==0 or y==0:
        break
    elif x.is_integer() == False or y.is_integer() == False:
        continue
    else:
        print(x*y)



