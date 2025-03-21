# ########################## Task 11
#  # # Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik
##### jako argument funkcji
# # # Utwórz funkcje Pion: która rysuje gwiazdki pionowo,
# ### liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # # Korzystając z w/w funkcji narysuj litery: E, L
### Użyj lambda, użyj wbudowanych funkcji, skróć maksymalnie kod programu, użytkownik, jako wejściowy argument podaje litere E lub L

from stars import horizontal, vertical

letter = input("Podaj litere E lub L: ").upper()

drawL = lambda x:(vertical(n),horizontal(n))
drawE = lambda x:(horizontal(n),vertical(n//2),horizontal(n),vertical(n//2),horizontal(n))

n = int(input("Podaj liczbe gwiazdek: "))

if letter =="E":
    drawE(n)
elif letter == "L":
    drawL(n)
else:
    print("Nieznana litera")
