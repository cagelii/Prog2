""" linked_list.py

Student: Carl Agelii
Mail: calle.agelii01@gmail.com
Reviewed by:
Date reviewed:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        pass

    def mean(self):               # Optional
        pass

    def remove_last(self):        # Optional
        pass

    def remove(self, x):          # Compulsory
        f = self.first
        if f.data == x:
            self.first = self.first.succ
            return True
        while f.succ:
            if x == f.succ.data:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False
        
    def count(self, x):           # Optional
        pass

    def to_list(self):            # Compulsory
        
        def _to_list(f):
            if f == None:
                return []
            return [f.data] +_to_list(f.succ)
        return _to_list(self.first)
    

    def remove_all(self, x):      # Compulsory       
        def _remove_all(f, x):
            if f == None:
                return 0
            if f.data == x:
                self.remove(x)
                return 1 + _remove_all(f.succ,x)
            else:
                return _remove_all(f.succ,x)
        return _remove_all(self.first, x)

    def __str__(self):            # Compulsary
        result = '('
        for x in self:
            result += str(x) + ', '
        if result[-1] != '(':
            result = result[:-2]
        result += ')'
        return result

    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
    The complexity is O(n^2), since insert goes through the entire list twice, because of insert.
    The list is already sorted, so it isn't necessary.
    '''

    def _copy(self):               # Compulsary
        res = LinkedList()         # Should be more efficient
        f = self.first
        if f:
            res.first = res.Node(f.data,f.succ)
        f = f.succ
        temp = res.first
        while f:
            temp.succ = res.Node(f.data,None)
            f = f.succ
            temp = temp.succ
        return res
                                    
    ''' Complexity for this implementation:
    Complexity is O(n) since it goes through the list once.

    '''

    def __getitem__(self, ind):   # Compulsory
        f = self.first
        for i in range(ind):
            f = f.succ
        return f.data       


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __eq__(self, __value: object) -> bool:
        return self.pnr == __value.pnr

    def __le__(self, __value: object) -> bool:
        return self.pnr <= __value.pnr

    def __lt__(self, __value: object) -> bool:
        return self.pnr < __value.pnr

    def __gt__(self, __value: object) -> bool:
        return self.pnr > __value.pnr

    def __ge__(self, __value: object) -> bool:
        return self.pnr >= __value.pnr



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:
    plist = LinkedList()
    p = Person("Calle",14)
    plist.insert(p)
    q = Person("Alicia",26)
    plist.insert(q)
    f = Person("Henrik",24)
    plist.insert(f)
    f = Person("Ante",12)
    plist.insert(f)
    print(plist)



if __name__ == '__main__':
    main()