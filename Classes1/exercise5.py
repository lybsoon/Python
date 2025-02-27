# 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
# użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = number1 + number2

if result % 2 == 0:
    print("number is even, result:", int(result / 2), "rest:", result % 2)
else:
    print("number is not even, result:", int(result / 2), "rest:", result % 2)
