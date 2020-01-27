import time
import random
# This is me tring some stuff i learnd, so the most thing could propably have been written better and 
# shorter also i can't really get an accurate runtime for the generator

print("Please choose which output you want to see \n")
choose = int(input("List = 1, with for = 2, with while = 3, Generator = 4, all = 5\n"))
rolls = int(input('Please choose a number for the amount of times you want to roll the dice\n'))
repeats = int(input("Please choose a number for the count of repeats\n"))


if choose < 0 or choose > 5:
    raise ValueError


def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("_" * 48)
        func(*args, **kwargs)
        print("_" * 48)
    return function_wrapper


def second():
    """
    using for
    """
    number = 0
    for b in range(rolls):
        randomnumber = random.randint(1, 6)
        number += randomnumber
    return number / rolls


def third():
    """
    using while
    """
    counter3 = 0
    t = 0
    while counter3 < (rolls + 1):
        t += random.randint(1, 6)
        counter3 += 1
    return t / rolls


def first():
    """
    using an array and append
    """
    array = []
    for q in range(rolls):
        array.append((random.randint(1, 6)))
    return sum(array) / rolls


time12 = time.time()


class Generator:
    """
    using a generator
    """
    def __init__(self):
        self.four = 0
        self.countergen = 0
        self.time9 = 0
        self.time10 = 0

    @staticmethod
    def randomnum():
        yield random.randint(1, 6)

    def fourth(self):
        while self.countergen < (rolls + 1):
            self.four += float(next(self.randomnum()))
            self.countergen += 1
        return self.four


c = Generator()


time1 = time.time()
for i in range(repeats):
    o = first()
time2 = time.time()

time3 = time.time()
for i in range(repeats):
    z = second()
time4 = time.time()

time5 = time.time()
for i in range(repeats):
    a = third()
time6 = time.time()

time7 = time.time()
for i in range(repeats):
    c.fourth()
time8 = time.time()
time11 = time.time()


@our_decorator
def output(chosen_type):
    """
    all the outputs with their times
    """
    print("number of diceroll: " + str(rolls))
    print("number of repeats: " + str(repeats))
    print("total throws per option: " + str(rolls * repeats) + "\n")

    if chosen_type == 1 or chosen_type == 5:
        print("calculation with list:")
        print("average = " + str(o))
        print("runtime = " + str(time2-time1) + "\n")

    if chosen_type == 2 or chosen_type == 5:
        print("calculation with for:")
        print("average = " + str(z))
        print("runtime = " + str(time4-time3) + "\n")

    if chosen_type == 3 or chosen_type == 5:
        print("calculation with while:")
        print("average = " + str(a))
        print("runtime = " + str(time6-time5) + "\n")

    if chosen_type == 4 or chosen_type == 5:
        print("calculation through Generator:")
        print("average = " + str(c.four/rolls))
        print("runtime = " + str(((time12 - time11) - (time8 - time7) - (time6 - time5) - (time4 - time3) - (time2 - time1)) * (-1)))


output(choose)
