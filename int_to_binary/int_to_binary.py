"""
1.     Write a method that takes in an integer and returns its binary representation in string form. So, if the input is 3 the output is '11', similarly if the input is 128, the output is '10000000'. Don't use the builtin 'bin' function for your solution.

Now enhance the output by adding a space to separate all the nibbles. This is how a calculator typically shows binary output. 128 would now look like this '1000 0000', and a number like 60 would look like this '11 1100'
"""

# note: I wanted to also test against negative numbers, but I wasn't able to find a good way to do so in the time I've given myself. I've looked into nibbles some, and I still don't fully understand how they work. 

from collections import deque

def int_to_binary(num):

    remainder_stack = deque()

    if num == 0:
        return '0'

    
    while num > 0:
        remainder = num % 2
        remainder_stack.appendleft(remainder)
        num = num // 2

    binary_num = ''
    while remainder_stack:
        binary_num += str(remainder_stack.popleft())

    return binary_num


