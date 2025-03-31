import random
from collections import Counter
from functools import reduce

languages = ["python","c#","java","dart","c++","kotlin"]

listProg = random.choices(languages, k =10000)

subLists = {}

for i ,name in enumerate(listProg):
    slice = i // 1000
    if slice not in subLists:
        subLists[slice] = []
    subLists[slice].append(name)


counter = [Counter(sublist) for sublist in subLists.values()]

result = reduce(lambda x,y: x+y,counter)

print(result)
