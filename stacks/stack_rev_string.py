"""
Loop through the string and push contents
Character by Character onto stack
"""
from stack import Stack
def rev_string(input_str):
    s=Stack()
    index=0
    while index in range(len(input_str)):
        s.push(input_str[index])
        index+=1
    rev_str=''
    while not s.is_empty():
        rev_str+=s.pop()
    return rev_str
print(rev_string('YOB'))


    
