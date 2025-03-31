## b) programuj funkcyjnie

import random


languages = ["python","c#","java","dart","c++","kotlin"]

listProg = random.choices(languages, k =10000)

def counterLanguage(list,name):
    counter = 0
    for i in list:
        if i == name:
            counter +=1
    return counter

print(listProg)
print(counterLanguage(listProg,"dart"))