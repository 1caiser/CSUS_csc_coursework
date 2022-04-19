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
# S → <AB
# A → aAb | b
# B → bB | >
def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()
        tok = toks.next()
        if tok == None:
            raise Exception
        elif top in ('<', 'a', 'b', '>'):
            toks.match(top)
        elif top == 'S' and tok == '<':
            stack.append('B')
            stack.append('A')
            stack.append('<')
        elif top == 'A' and tok == 'a':
            stack.append('b')
            stack.append('A')
            stack.append('a')
        elif top == 'A' and tok == 'b':
            stack.append('b')
        elif top == 'B' and tok == 'b':
            stack.append('B')
            stack.append('b')
        elif top == 'B' and tok == '>':
            stack.append('>')
        else:
            raise Exception
    if toks.next() != None:
        raise Exception

try:
    parse("<aaabbbb>")
except:
    print("rej")
else:
    print("acc")