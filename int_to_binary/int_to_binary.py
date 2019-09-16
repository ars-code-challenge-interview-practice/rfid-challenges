"""
1.     Write a method that takes in an integer and returns its binary representation in string form. So, if the input is 3 the output is '11', similarly if the input is 128, the output is '10000000'. Don't use the builtin 'bin' function for your solution.

Now enhance the output by adding a space to separate all the nibbles. This is how a calculator typically shows binary output. 128 would now look like this '1000 0000', and a number like 60 would look like this '11 1100'
"""

def __init__(self):
    self.num = None


def int_to_binary(self, num):
    modulo_two_arr = []

    while num < 0:
        modulo_two = num % 2
        modulo_two_arr.append(modulo_two)
        div_by_two = num // 2

    return num


# get the algorithm
# return that integer as a string
# then worry about spaces


