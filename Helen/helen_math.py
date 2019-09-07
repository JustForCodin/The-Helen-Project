#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import decimal
import math

def draw_parabola_graph():
    x = np.arange(int(input("Value 1: ")), int(input("Value 2: ")))
    print("X values: ", x)
    y = x**2
    print("Y values: ", y)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

#draw_parabola_graph()

def draw_hiperbola_graph():
    x_min = int(input("Enter the x minimum value: "))
    x_max = int(input("Enter the x maximum value: "))
    del_x = float(input("Enter the decimal x value: "))
    n = int(input("Enter the numerator value: "))

    x = np.around(np.arange(x_min, x_max, del_x), decimals=4)
    print("Xs: ", x)
    y = n / x
    print("Ys", y)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    plt.grid(False)
    plt.plot(x, y)
    plt.show()

#draw_hiperbola_graph()

def draw_sqtx_function():
    x = np.arange(int(input("Enter value 1: "), int(input("Enter value 2: "))))
    y = math.sqrt(x)
    print(y)
#draw_sqtx_function()
######## TESTS ZONE ###########




