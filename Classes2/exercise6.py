# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)

m = int(input("podaj wartosc n: "))
result = 0
suma = 1

for i in range(1,m+1):
    suma += 1
    result += suma
print("suma wynosi:", result)

