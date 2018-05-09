print('+---------------------+')
print('| DATATYPES IN PYTHON |')
print('+---------------------+')
'''
Python is loosely typed language.
No need to define datatype to use the variables.
There are 2 types. Mutable and Immutable
Immutable types - Numbers, Strings and Tuples
Mutable types - Lists, Dictionaries, Sets

Numeric Types - Integer, Float and Complex (number + imaginary part. Imaginary part if represented by suffix 'j' ex: 3+4j. operations ex: (3+4j)+(1+2j)=(4+6j)
Strings - use ' or " quotes for single line '''''' (six 's) for multiple lines
multi='''''' this is a
multiline text string''''''

Operations on string
concatenation 'a'+'b'='ab'
repetition 'a'*2='aa'
slicing string1='abcd', abcd[1:2]='bc'
indexing string1='abc' string1[1]='b'
find() str='asdf' str.find('a')=0//index of position -1 if not found
replace str='asdf' str.replace('df','h')='ash'
split() str='a,b,c' str.split(',')={a,b,c}
count() str='aabc' str.count('a',beg=0,end=4)=2
upper() - convert to upper case
max(string) - get the higher word in ascii table
min(string) - get the least char in ascii table
isalpha() - check if it is alphanumeric

Tuple - a sequence of immutable python objects
myTuple = ('abc', 1, 5.6,'xyz')
tuple operations
concatenation tup=('a','b'), tup+('d')=(a,b,d)
repetition tup=(a,b), tup*2=(a,b,a,b)
slicing tup=(a,b,c) tup[1:2]=(b,c)
indexing tup=(a,b,c) tup[0]=a

Lists - collection of python objects
myList=['ab',1,4.5,'sd']
List operations
append ls=[a,b,c] ls.append(d)=> ls=[a,b,c,d]
extend(list) ls=[a,b,c] ls2=[x,y,z], ls.extend(ls2)=> [a,b,c,x,y,z]
pop() ls=[a,b,c] ls.pop()=[a,b], ls.pop()=[a]
insert(index, value) ls=[a,b,c] ls.insert(2,d)=> ls=[a,b,d,c]

Dictionary - a flexible data type. ordered. no duplciates. only latest values are stored
mydict={}/{1:a,2:b}/{a:b,1:[a,b,c]}/dict([(1,a),(2,b)])
Dictornary Operations
mydict= {1:a,2:b,a:b}
Access- mydict[1]=>a
length() mydict.len()=3
key() mydict.key()=[1,2,a]
values() mydict.values()=[a,b,b]
items() mydict.items()=[(1,a),(2,b),(a,b)]
get(key) mydict.get(1)=a
update(dict) mydict.update({5:c})={1:a,2:b,a:b,5:c}
pop() mydict.pop(3)={1:a} //pop last 3 items

Sets- unordered collection of items. no duplicates. all elements are immutable
myset={1,2,3,5,4}
Operations
s1={1,2,3}, s2={3,a,b}
union s1|s2={1,2,3,a,b}
intersection s1&s2={3}
difference s1-s2={1,2}//in set 1 but not in set2
'''

print('\n--- Numbers ---')
type='Integers'
num1=10
num2=20
res=num1+num2
print('{type:10s} => {num1} + {num2} = {res}'.format(**locals()))#one way of formatting
type='Float'
num1=10.25
num2=20.43
res=num1+num2
print('{type:10s} => {num1} + {num2} = {res}'.format(**locals()))
type='Complex'
num1=10+51j
num2=20+82j
res=num1+num2
print('{type:10s} => {num1} + {num2} = {res}'.format(**locals()))

print('\n--- String operations ---')
string1='abcd '
string2='efgh'
print(string1,' + ', string2,' = ',string1+string2)
print(string1,' * ', 2,' = ',string1*2)
print(string1,' slice 1,2  = ',string1[1:2])
print(string1,' slice ,2  = ',string1[:2])
print(string1,' slice 1,  = ',string1[1:])
print(string1,' slice 1,-3  = ',string1[1:-3])
print(string1,' slice 1,-2  = ',string1[1:-2])
print(string1,' slice 1,-1  = ',string1[1:-1])
print(string1, ' index 2 = ',string1[2])
print(string1, ' count a = ',string1.count('a'))
print(string1, ' count A = ',string1.count('A'))
print(string1, ' find c = ',string1.find('c'))
print(string1, ' replace c = ',string1.replace('c','x'))
print(string1, ' split c = ',string1.split('c'))
print(string1, ' count c = ',string1.count('c'))
print(string1, ' upper = ',string1.upper())
print(string1, ' lower = ',string1.lower())
print(string1, ' max = ',max(string1))
print(string2, ' min = ',min(string2))
print(string1, ' isapha = ',string1.isalpha())#false as it has a space
print(string2, ' isapha = ',string2.isalpha())

print('\n--- Tuples (immutable)---')
tup1=('abc',1,3.2,'xyz')
tup2=('abc',5.6)
print('Tuple#1: ',tup1)
print('Tuple#2: ',tup2)
print(tup1,' concat ',tup2,' = ',tup1+tup2)
print(tup1,' repeat 2 times = ',tup1*2)
print(tup1,' slicing from 1 to 3 (2 elements) = ',tup1[1:3])
print(tup1,' value at index 3 = ',tup1[3])

print('\n--- List and Operations ---')
list1=['ab','cd','pq']
list2=['xy',1,10.4,5+2j]
print('List#1: ',list1)
print('List#2: ',list2)
print(list1,' append a')
list1.append('a')
print('New List#1: ',list1)
list1.extend(list2)
print('Extended List#1 with List#2: ',list1)
print(list1, ' popped item: ',list1.pop())
print(list1, ' pop 3rd item from last: ',list1.pop(3))
print(list1, ' after inserting x at index 0: ',list1.insert(0,'x'))
print(list1, ' after inserting y at index -1: ',list1.insert(-1,'y'))

print('\n--- Dictionary ---')
#mydict={}/{1:a,2:b}/{a:b,1:[a,b,c]}/dict([(1,a),(2,b)])
mydict= {1:'a',2:'b','a':'b'}
print('Dictionary: ',mydict)
print('mydict[1]: ',mydict[1])
print('Length: ',len(mydict))
print('Keys in Dict: ',mydict.keys())
print('Values in Dict: ', mydict.values())
print('Items in Dict: ', mydict.items())
print('mydict.get(1): ',mydict.get(1))
print('mydict.update({5:c}): ',mydict.update({5:'c'}))
print('Dict after update: ',mydict)
print('Pop item with key 5: ',mydict.pop(5))
print('Dict after pop: ',mydict)

print('\n--- Sets ---')
s1={1,2,3,5,4,5}#duplicates are ignored
s2={3,'a','b'}
print('Set#1: ',s1)#prints in order
print('Set#2: ',s2)
print('Union of sets: ',s1|s2)
print('Intersection of sets: ',s1&s2)
print('Difference of s1 and s2: ',s1-s2)#in set1 but not in set2
print('Difference of s2 and s1: ',s2-s1)#in set2 but not in set1
