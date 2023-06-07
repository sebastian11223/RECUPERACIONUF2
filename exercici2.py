import random

import numpy as np

def ex2part1():

    a = np.array([random.randint(20, 90),random.randint(20, 90),random.randint(20, 90),random.randint(20, 90)])

    return a

print(ex2part1())

def ex2part2():
    b = np.array([[random.uniform(20,80),random.uniform(20,80),random.uniform(20,80)],[random.uniform(20,80),random.uniform(20,80),random.uniform(20,80)]])

    return b
print(ex2part2())


def ex2part3():

    b = np.array([random.randint(0, 15),random.randint(0, 15),random.randint(0, 15),random.randint(0, 15)]).reshape(-1, 1)

    return b
print(ex2part3())