## Utwórz listę zawierającą 10000 losowych nazw 6 języków programowania
## np. list_prog = ['python','java','C++','C++','python',....,'java']
# oblicz ile razy wybrany język programowania wystąpił w liście
## a) programuj imperatywnie

import random


languages = ["python","c#","java","dart","c++","kotlin"]

listProg = random.choices(languages, k =10000)

counter = 0

for i in listProg:
    if i =="python" in listProg:
        counter +=1

print(listProg)
print(counter)

