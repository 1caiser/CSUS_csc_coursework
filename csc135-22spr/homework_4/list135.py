from numpy import sort

class list135:
    
    def __init__(self, first_item = None, rest_of_list = None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list

    def cons(self, first_item):
        return list135(first_item, self)
    
    def first(self):
        return self._first_item
    
    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None
        
    def __str__(self):
        result = "["
        cur = self
        if cur._rest_of_list != None:
            result = result + str(cur._first_item)
            cur = cur._rest_of_list
        while cur._rest_of_list != None:
            result = result + "," + str(cur._first_item)
            cur = cur._rest_of_list
        # if len(result) == 1:
        #     result = result + str(cur._first_item)
        # else:
        #     result = result + "," + str(cur._first_item)
        return result + "]"
    
    # sorted

    def sorted(self):
        my_list = []
        my_iter = self
        if self._first_item == None or self._rest_of_list == None:
            return my_list
        else:
            while my_iter._rest_of_list != None:
                my_list.append(my_iter._first_item)
                my_iter = my_iter._rest_of_list
            return sorted(my_list)
    
    def sorted135(self):
        my_list = []
        my_iter = self
        if self._first_item == None or self._rest_of_list == None:
            return self
        else:
            while my_iter._rest_of_list != None:
                my_list.append(my_iter._first_item)
                my_iter = my_iter._rest_of_list
            my_list = sorted(my_list)
            acc = list135(len(my_list))
            x = range(len(my_list)-1, -1, -1)
            for e in x:
                acc = acc.cons(my_list[e])
            return acc

# Write a tail recursive function "reverse" that takes a list135 
# parameter and returns a list135 that is the same as the parameter 
# but in reverse order. For example [1,2,3] would reverse to [3,2,1].

# Your solution should use a design similar to fact and _fact shown 
# above. The accumulator should be initialized as an empty list, and
# the invariant that you maintain should be that the reversal of the
# list parameter followed by the accumulator should equal the 
# reversal of the original list.

# Do not place this method in your class. Instead it should use the 
# list135 public interface to manipulate the old and new lists.

def _reverse(lst, acc):
    if lst.rest() is None:
        return acc
    else:
        acc = acc.cons(lst.first())
        return _reverse(lst.rest(),acc)

def reverse(lst):
    return _reverse(lst,list135())

# Beginning with your tail recursive solution to _reverse, convert
# it to a loop version.

def l_reverse(lst,acc):
    if lst.rest() is None:
        return lst
    else:
        cur = lst
        while cur.rest() is not None:
            acc = acc.cons(cur.first())
            cur = cur.rest()
        return acc