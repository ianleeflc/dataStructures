"""
 usa a stack to check whether or not a string has balanced usage of parenthesis
 example of balanced ones: ({{[]}})
 example of unbalanced ones: ((), ))
"""

# the first version, has some flaws
from stack import Stack
def is_match(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    else: 
        return False
def is_paren_balanced(paren_string):
    index=0
    is_balanced=True
    s=Stack()
    while index<len(paren_string) and is_balanced==True:
        if paren_string[index] in '([{':
            s.push(paren_string[index])
        else: 
            if is_match(s.pop(), paren_string[index]):
                is_balanced=True
            else: 
                is_balanced=False
                return False
        index+=1
    if s.is_empty() and is_balanced==True:
        return True

print(is_paren_balanced('[]')) # works
print(is_paren_balanced('([{}])')) # works
print(is_paren_balanced('(([)')) # works
print(is_paren_balanced('())')) # doesn't work
print(is_paren_balanced('))')) # doesn't work

# the imporoved version
from stack import Stack
def is_match(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    else: 
        return False
def is_paren_balanced(paren_string):
    index=0
    is_balanced=True
    s=Stack()
    while index<len(paren_string) and is_balanced==True:
        if paren_string[index] in '([{':
            s.push(paren_string[index])
        else: 
            if s.is_empty(): # case of '())', or '))', or '', or all popped and done
                is_balanced=False
                return False
            elif is_match(s.pop(), paren_string[index]):
                is_balanced=True
            else: 
                is_balanced==False
                return False
        index+=1
    if s.is_empty() and is_balanced==True:
        return True

print(is_paren_balanced('[]')) # works
print(is_paren_balanced('([{}])')) # works
print(is_paren_balanced('(([)')) # works
print(is_paren_balanced('())')) # works
print(is_paren_balanced('))')) # works

      



