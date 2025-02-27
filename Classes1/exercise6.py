# 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
# iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


def sum_(nr1, nr2):
    return nr1 + nr2


def difference(nr1, nr2):
    return nr1 - nr2


def quotient(nr1, nr2):
    return nr1 / nr2


def product(nr1, nr2):
    return nr1 * nr2


def power(nr1, nr2):
    return nr1 ** nr2


print("sum of numbers:", sum_(number1, number2))
print("difference of numbers:", difference(number1, number2))
print("quotient of numbers:", quotient(number1, number2))
print("product of numbers:", product(number1, number2))
print("power of numbers:", power(number1, number2))
