"""
Solutions to module 4
Student: Carl Agelii
Mail: calle.agelii01@gmail.com
Reviewed by: Naser
Reviewed date:2023-10-11
"""

import math
import numpy as np
import functools as ft
from matplotlib import pyplot as plt
from time import perf_counter as pc
import concurrent.futures as future

def piApprox(n):
    ncx = []
    ncy = []
    nsx = []
    nsy = []
    ys = np.random.uniform(-1,1, n)
    xs = np.random.uniform(-1,1, n)
    for i,_ in enumerate(xs):
        if xs[i]**2+ys[i]**2 <= 1:
            ncx.append(xs[i])
            ncy.append(ys[i])
        else:
            nsx.append(xs[i])
            nsy.append(ys[i])
    pi = (4*len(ncx)/n)
    fig,ax = plt.subplots(figsize=(5,5))
    ax.plot(nsx,nsy,'bo')
    ax.plot(ncx,ncy,'ro')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    print(f"Number of dots inside the circle for {n} dots: {len(ncy)}. Approximate pi= {pi}")
    print(f'Exact pi: {math.pi}')
    plt.show()
    return(piApprox)
    

def nVolume(n,d):
    vd = lambda d: math.pi**(d/2)/(math.gamma((d/2)+1))
    exact = vd(d)
    xs = np.random.uniform(-1,1,size=(n,d))
    norm = []
    for x in xs:
        norm.append(ft.reduce(lambda y,z: y+z, map(lambda t: t**2,x)))  
    xinside = len(list(filter(lambda x: x<=1,norm)))
    approx = 2**d*xinside/n
    print(f'Approximate volume of a {d}-dimensional ball is: {approx}. The exact volume is: {exact}')
    return approx


def main():
    # 1.1
    ns = [1000, 10000, 100000]
    for n in ns:
        piApprox(n)

    # 1.2
    nVolume(100000,2)
    nVolume(100000,11)

    # 1.3
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        d = 11
        n = 1000000
        ds = []
        ns = []
        for i in range(10):
            ds.append(d)
            ns.append(n)
        results = ex.map(nVolume, ns, ds)

    end = pc()
    time = round(end - start,3)
    print(f'Time for parallel: {time}')

    start = pc()
    nVolume(10000000,11)
    end = pc()
    time = round(end - start,3)
    print(f'Time for regular: {time}')

if __name__ == "__main__":
    main()