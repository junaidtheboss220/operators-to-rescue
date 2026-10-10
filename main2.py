"""1. Bitwise Operators
"Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name."

For example, 2 is 10 in binary and 7 is 111.

Operator	Description
&	Bitwise AND
|	Bitwise OR
~	Bitwise NOT
^	Bitwise XOR
>>	Bitwise right shift
<<	Bitwise left shift"""

A = 60
B = 13
# 60 = 0011 1100
# 13 = 0000 1101


c = A & B# 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = A | B
print("Line 2 - Value of c is ", c)
