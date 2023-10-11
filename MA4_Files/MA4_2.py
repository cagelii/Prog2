#!/usr/bin/env python3.9

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	


@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	n = list(range(30,35))
	times_py = []
	times_numba = []
	times_cpp = []
	for i in n:
		start = pc()
		fib_py(i)
		stop = pc()
		times_py.append(stop-start)

		start = pc()
		fib_numba(i)
		stop = pc()
		times_numba.append(stop-start)

		f = Person(i)
		start = pc()
		f.fib()
		stop = pc()
		times_cpp.append(stop-start)

	fig,ax = plt.subplots()
	ax.plot(n,times_py,label='Pure python')
	ax.plot(n,times_numba,label='Numba')
	ax.plot(n,times_cpp, label='cpp')
	ax.legend()
	plt.savefig("times.png")
if __name__ == '__main__':
	main()
