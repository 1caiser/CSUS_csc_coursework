class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise pass over the current one and move to the next.
    def match(self,s):
        if (self._i < len(self._toks)) and (self._toks[self._i] == s):
            self._i += 1
        else:
            raise Exception
            
    # If any tokens remain return the current one. If no more, return None.
    def next(self):
        if self._i < len(self._toks):
            return self._toks[self._i]
        else:
            return None


# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.

# S' → S$
# S → BA
# A → +BA | -BA | λ
# B → DC
# C → *DC | /DC | λ
# D → a | (S)

def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()      # Always pop top of stack
        tok = toks.next()      # None indicates token stream empty
        if top in ('+', '-', '*', '/', '(', ')', 'a'):     # Matching stack top to token
            toks.match(top)
        elif top == 'S':
            stack.append('A')
            stack.append('B')
        elif top == 'A' and tok == '+':
            stack.append('A')
            stack.append('B')
            stack.append('+')
        elif top == 'A' and tok == '-':
            stack.append('A')
            stack.append('B')
            stack.append('-')
        elif top == 'A' and tok == None: # next == $ 
            pass # "pass" is how you say do nothing in Python

        
        elif top == 'B' and tok == 'D':
            stack.append('C')
            stack.append('D')
        
        elif top == 'C' and tok == '*':
            stack.append('C')
            stack.append('D')
            stack.append('*')
        elif top == 'C' and tok == '/':
            stack.append('C')
            stack.append('D')
            stack.append('/')
        elif top == 'C' and tok == None: # next == $ 
            pass # "pass" is how you say do nothing in Python

        elif top == 'D' and tok == 'a':
            stack.append('a')
        elif top == 'D' and tok == '(':
            stack.append(')')
            stack.append('S')
            stack.append('(')
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception

try:
    parse("<aaabbbb>")
except:
    print("rej")
else:
    print("acc")