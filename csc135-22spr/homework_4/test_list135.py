from list135 import *
from list135 import list135

# testing reverse() et al
test_reverse = True
if test_reverse == True:
    a = list135().cons(2).cons(5).cons(3).cons("hello").cons("world")

    print(a)
    print(reverse(a))
    print(l_reverse(a,list135()))

# testing sorted() et al
test_sorted = False
if test_sorted == True:
    a = list135()
    b = a.cons(2)
    c = b.cons(-6)
    d = c.cons(5)
    e = d.cons(4)

    print(e)
    print(e.sorted())
    print(e.sorted135())