print('+---------------------+')
print('| FUNCTIONS IN PYTHON |')
print('+---------------------+')

'''
procedure style.
has reusable code. reduces redundency.
syntax
def <name>(<args>):
    <function body>
    return <value>#optional
functions use call by reference
'''
#fabonocci series
print('--- Basic Definition ---')
def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b+=a
        print(a)
    return b
num=5
print(fibo(num))
