from random import *


def randlist(list):
    loops = 0
    while loops < 10:
        num = randint(0, 9)
        if num not in list:
            list.append(num)
            loops += 1
    return list


chiefs = []
bucks = []
print(randlist(chiefs))
print(randlist(bucks))

