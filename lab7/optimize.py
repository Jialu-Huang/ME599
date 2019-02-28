#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import random as random
from scipy.optimize import fmin

def f(x):
    return -x ** 2 - 3 * x + 6

def optimize_step(f,bounds_low,bounds_up,n):
    x = np.linspace(bounds_low,bounds_up,n)
    #print(x)
    largest_value1 = x[0]
    for i in range (len(x)-1):
        if f(x[i]) <= f(x[i+1]):
            largest_value1 = x[i+1]
            #x_max = x[i+1]
        #print(largest_value1)
        #plt.plot(f(x), '-x', label="Function Plot")
    return largest_value1

def optimize_random(f,bounds_low,bounds_up,m):
    #print(m)
    largest_value2 = (bounds_low+bounds_up)/2
    #print(largest_value2)
    for i in range (m):
        x = random.uniform(bounds_low, bounds_up)
        if f(x) - f(largest_value2) >= 0:
            largest_value2 = x
        #plt.plot(f(x), '--x', label="Function Plot")
    return largest_value2

def fmax(x):
    return float(0 - f(x))

def optimize_fmax(fmax,bounds_low,bounds_up):
    #x = np.linspace(bounds_low, bounds_up, n)
    # print(x)
    largest_value3 = fmin(fmax,(bounds_low+bounds_up)/2,disp=0)[0]
    if largest_value3 <= bounds_low or largest_value3 >= bounds_up:
        if fmax(bounds_low) >= fmax(bounds_up):
            largest_value3 = (bounds_up)
        else:
            largest_value3 = (bounds_low)
    return largest_value3

#def fmul(x,y,z,u):
    #return x+y+z+u

#def optimize_md(fmul,[(),(),(),]):


if __name__ == '__main__':
    maxvalue1 = optimize_step(f, -10, 100, 5000)
    print(maxvalue1)
    maxvalue2 = optimize_random(f, -10, 100, 5000)
    print(maxvalue2)
    maxvalue3 = optimize_fmax(fmax,-10,100)
    print(maxvalue3)

    di1 = []
    di2 = []
    di3 = []
    #n = [ii for ii in range(10, 100, 20)]
    # print(n)
   # for i in n:
   #     maxvalue1 = optimize_step(f, 10, 100, i)
   #     maxvalue2 = optimize_random(f, 10, 100)
   #     maxvalue3 = optimize_fmax(fmax, x_maxindex)
   #     di1.append(abs(maxvalue1 - maxvalue3))
   #     di2.append(abs(maxvalue2 - maxvalue3))
   #     di3.append(abs(maxvalue1 - maxvalue2))

    #plt.plot(n, di1, '-x', label="the difference between step and fmax")
    #plt.plot(n, di2, '--x', label="the difference between random and fmax")
    #plt.plot(n, di3, '--x', label="the difference between step and random")
    #plt.xlabel('Numbers')
    #plt.ylabel('Error Value')
    #plt.legend()
    #plt.title('Absolute Error of functions Plot')
    #plt.show()

    #plt.xlabel('Number')
    #plt.ylabel('Value')
    #plt.legend()
    #plt.title('Function Plot')
    #plt.show()
