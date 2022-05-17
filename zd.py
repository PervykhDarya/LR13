#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process
import math


eps = .0000001


def sum(x):
    n = 1
    s = 1
    curr = 1
    previous = 0
    while True:
        if abs(s - previous) < eps:
            break
        curr = curr * (n + 1) * x
        previous = s
        s += curr
        n += 1
        if n > 6:
            break

    print(f"Сумма ряда для значения {x}: {s}")
    print(f"Проверка: 1/(1 - {x})^2 = {1 / math.pow((1 - x), 2)}")

if __name__ == '__main__':
    process1 = Process(target=sum, args=(-0.7,))
    process1.start()
    process2 = Process(target=sum, args=(3,))
    process2.start()