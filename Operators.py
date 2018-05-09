#Simple comment
'''
multi line
comments
'''
print('+---------------------+')
print('| OPERATORS IN PYTHON |')
print('+---------------------+')
num1=5
num2=4
#Arith Operations
print('---Arithmetic Operators---')
print(num1,' + ', num2 , ' = ', num1+num2)
print(num1,' - ', num2 , ' = ', num1-num2)
print(num1,' * ', num2 , ' = ', num1*num2)
print(num1,' / ', num2 , ' = ', num1/num2)
print(num1,' % ', num2 , ' = ', num1%num2)
print(num1,' ^ ', num2 , ' = ', num1**num2)
print(num1,' // ', num2 , ' = ', num1//num2)

#Assignment operations
print('\n---Assignment Operators---')
num3=num1+num2
num4=0
num4+=num1#throws error when num4 is undefiend
print('regular add = ',num3)
print('shorthand add = ',num4)

#Comparision
print('\n---Comparision Operators---')
print(num1,' > ', num2,'? ',num1>num2)
print(num1,' < ', num2,'? ',num1<num2)
print(num1,' <= ', num2,'? ',num1<=num2)
print(num1,' >= ', num2,'? ',num1>=num2)
print(num1,' == ', num2,'? ',num1==num2)
print(num1,' != ', num2,'? ',num1!=num2)

#Logical Operators
print('\n---Logical Operators---')
x=True
y=False # boolean values start with Caps value
print(x,' and ',y,' = ',x and y)
print(x,' or ',y,' = ',x or y)
print('!',y,' = ', not y)

#Bitwise Operators
print('\n---Bitwise Operators---')
# |-or, &-and, ^-xor
print(num1,'|',num2,' = ',num1|num2)#101 | 100 = 101
print(num1,'&',num2,' = ',num1&num2)#101 & 100 = 100
print(num1,'^',num2,' = ',num1^num2)#101 ^ 100 = 001
#left and right shift
print(num1,'>>',2,' == ',num1>>2)#00000101 >> 2 = 00000001
print(num2,'<<',2,' == ',num1<<2)#00000100 << 2 = 00010000 -result is 20?
print(num1,'>>',1,' == ',num1>>1)#00000101 >> 1 = 00000010
print(num1,'<<',1,' == ',num1<<1)#00000101 << 1 = 00001010

#Identity Operators
print('\n---Identity Operators---')
# is and is not
print(num1,' is ',num2,' = ',num1 is num2)
print(num1,' is ',5,' = ',num1 is 5)
print(num1,' is not ',num2,' = ',num1 is not num2)
print(num1,' is not ',5,' = ',num1 is not 5)

#Membership Operators
print('\n---Membership Operators---')
#used in lists - a collection of objects
# in and not in
list=[1,2,3,4,5]
print(2,' in ',list,' = ',2 in list)
print(6,' in ',list,' = ',6 in list)
print(2,' not in ',list,' = ',2 not in list)
print(6,' not in ',list,' = ',6 not in list)

