print('+-----------------------------------+')
print('| FLOW CONTROL STATEMENTS IN PYTHON |')
print('+-----------------------------------+')

'''
7 flow control statements
if, if-else, if-elif-else, for, while, break, continue
'''
print('--- IF Statement ---')
marks=75
print('Marks=',marks)
if(marks>80):
    print('Grade A')#this will not print
print('--end of  if')
if(marks>=80):
    print('Grade A')
elif (marks>60 and marks<80):
    print('Grade B')
else:
    print('Grade C')
print('--end of  if-elif-else')

print('\n--- Looping Statement ---')
print('\n--- While loop ---')
count=int(input('Enter number: '))
if (count>0):
    while(count>0):
        print('loop value: ',count)
        count-=1
else:
    print('Enter number greater than 0')
#get input from user
print('\n--- For loop ---')
#for var name in sequence
#99 beer song
#range(start,end,increment value) - will give the list of values from start till end with increment value
for qty in range(5,0,-1):#start from 99 till 0 by decrementing by -1
    if qty>1:
        print(qty,' bottles of beer on the wall,',qty,'bottles of beer')
        if qty>2:
            suffix=str(qty)+'bottles of beer on the wall'
        else:
            suffix='1 botton of beer on the wall'
    elif qty==1:
        print('1 bottle of beer on the wall, 1 bottle of beer')
        suffix=' no more beer on the wall'
    print('take one down and pass it around', suffix)
    print('---')
#break statements
print('\n--- Break and Continue ---')
count=0
while True:
    print(count)
    count+=1
    if count>5:
        break
print('end infinite while loop')
print('list all odd numebrs less than ', count)
for x in range(count):
    if x%2==0:
        continue
    print(x)
print('end for loop-contiune')