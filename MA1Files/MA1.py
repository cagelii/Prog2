"""
Solutions to module 1
Student: Carl Agelii
Mail: calle.agelii01@gmail.com
Reviewed by:Behnam
Reviewed date:2023-09-07
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def power(x, n: int):                        # Optional
    """ Computes x**n using multiplications and/or division """
    pass


def multiply(m: int, n: int) -> int:         # Compulsory
    """ Computes m*n using additions"""
    if m == 0:
        return 0 
    elif m == 1:
        return n
    else:
        return n + multiply(m-1,n)


def divide(t: int, n: int) -> int:           # Optional
    """ Computes m*n using subtractions"""
    pass


def harmonic(n: int) -> float:                 # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1) 


def digit_sum(x: int, base=10) -> int:       # Optional
    """ Computes and returns the sum of the decimal (or other base) digits in x"""
    pass


def get_binary(x: int) -> str:               # Compulsary
    """ Returns the binary representation of x """
    minus = False
    if x < 0:
        x = abs(x)
        minus = True
    def get_binary_(n):
        if n == 0:
            return '0'
        elif n == 1:
             return '1'
        else:
            return str(get_binary_(n//2))+str(n%2)
    if minus:
        return '-' + get_binary_(x)
    else:
        return get_binary_(x)
    



def reverse_string(s: str) -> str:           # Optional
    """ Returns the s reversed """
    pass


def largest(a: iter):                        # Compulsory
    """ Returns the largest element in a"""
    if len(a)==1:
        return a[0]
    else:
        if a[-1]>largest(a[:-1]):
            return a[-1]
        else:
            return largest(a[:-1])


def count(x, s: list) -> int:                # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    elif s[-1] == x:
        return count(x, s[:-1])+1
    elif type(s[-1]) == list:
        return count(x,s[-1])+ count(x,s[:-1])
    else:
        return count(x,s[:-1])


def zippa(l1: list, l2: list) -> list:       # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if len(l1) == 0 or len(l2) == 0:
        return l1 + l2
    else:
        return [l1[0], l2[0]] + zippa(l1[1:],l2[1:])


def bricklek(f: str, t: str, h: str, n: int) -> str:  # Compulsory
    """ Returns a string of instruction ow to move the tiles """
    if n == 0:
        return []
    return bricklek(f,h,t,n-1) + [f"{f}->{t}"] + bricklek(h,t,f,n-1)

def fib(n: int) -> int:                       # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')
    
    print('\n\nCode for analysing fib\n')
    t = []
    for number in [31,32]:
        tstart = time.perf_counter()
        fib(number)
        tstop = time.perf_counter()
        t.append(tstop-tstart)
    print(f"Time for 32st fibonacci number divided by 31st: {t[1]/t[0]}")
    c = t[0]/(1.618**31)
    #print(c)
    print(f"Approximated time for 50th number: {c*(1.618**50)/(60*60*24)} days")
    print(f"Approximated time for 100th number: {c*(1.618**100)/(60*60*24*365)} years")

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  It would take 2^50-1 seconds. 
  
  
  
  
  
  Exercise 17: Time for Fibonacci:
  I verified by dividing the time for F(n=32) by F(n=31) and got 1.613170 on my computer at home.
  I calculated the constant c by taking dividing the time it took to compute by 1.618^31. I could then calculate the time for 50 and 100 iterations.
  
  
  
  Exercise 20: Comparison sorting methods:
  1 second for 1000 random numbers. 
  Insertion sort: t(n) = c1*n^2 => 1 = c1*1000^2 => c1 = 10^-6
  Time for 10^6 = 10^-6 * 10^(6*2) = 10^6 sec
  Time for 10^9 = 10^-6 * 10^(9*2) = 10^12 sec
  
  Merge sort: t(n) = c2*n*log(n) => c2 = 1/3000 
  Time for 10^6 = 10^-6 * 10^6 * log(10^6) = 6 sec
  Time for 10^9 = 10^-6 * 10^9 * log(10^9) = 9 * 10^3
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  tA(n) = n
  tB(n) = c*n*log(n), tB(10) = 1 = c*10*log(10) = 10*c => c = 1/10
  tA(n) < tB(n) => n < n*log(n)/10 => 10 < log(n) => n > 10^10
  
  
  
  
  
  





"""
