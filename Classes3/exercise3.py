word = str(input("Podaj slowo: "))
litera = str(input("podaj litere: "))
resultLambda = lambda letter: litera in letter

print(resultLambda(word))