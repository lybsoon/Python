### Utwórz pętlę generującą 50 liczb całkowitych z krokiem 5, większych niż 99
### Wykorzystaj count()

import itertools

counter = itertools.count(99,5)

for i, number in enumerate(counter):
    if i < 50:
        print(number)
    else:
        break