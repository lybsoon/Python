########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)

points = int(input("Podaj ilosc pkt: "))
max_points = 15

percent = round((points / max_points) * 100)

if percent in range(50, 60):
    print("Ocena 3")
elif percent in range(61, 70):
    print("Ocena 3.5")
elif percent in range(70, 81):
    print("Ocena 4")
elif percent in range(81,90):
    print("Ocena 4.5")
elif percent in range(91, 101):
    print("Ocena 5")
else:
    print("Ocena 2")