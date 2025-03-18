# ########################## Task 1
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

letters = ["K","a","c","p","e","r"]

resultLambda = lambda toWord: "".join(toWord)

print(resultLambda(letters))