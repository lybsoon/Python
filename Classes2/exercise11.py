## # ################################ Task 11
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)


word = str(input("Podaj haslo: "))
passwords = ("adam123", "SzybkiSzymek")

if word in passwords:
    print("Zalogowano: Kacper Breczko")
else:
    print("Nie prawidlowe haslo")