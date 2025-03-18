# ########################## Task  2
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string

Name = "Kacper Breczko"

splitWords = lambda name: name.split(" ")
splitLetters = lambda name: list(name)

print(splitWords(Name))
print(list(splitLetters(Name)))

