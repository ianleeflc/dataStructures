"""
Study binary basics if you don't know how to do this
"""
from stack import Stack
def div_by_two(dec_num):
    s=Stack()
    bin_num=''
    while dec_num>0: 
        remainder=dec_num%2
        dec_num=dec_num//2
        s.push(remainder)
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num
print(div_by_two(256))
