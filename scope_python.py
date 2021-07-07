# scope

x = 1 #here everthing is in global scope
y = 1 #here everthing is in global scope

#indisde functions the new variables( defined inside the functions) are local scoped
#which mean you cannot access the uotside the function
def foo():
    z = 1
    print(f'z here in function is {z}')
    print('===================================')
    def boo():
        print('boo')
        print(z, 'inside boo')
    boo()

foo()

#foo and foo2 doesn't know each other(brothers) but bouth of them know 'x' and 'y' thier parents
def foo2():
    z = 2
    print(f'z here in function is {z}')
    print('===================================')
    #print boo - error, out of scope

#for loop desn't have a scope
for x in range(1,10):
    #insdent inside for does not scope
    y = x +1
    print(x)

while True:
    x1 = 12
    break
print('=========================================')
print(x)
print(y)
print(x1)

#print('outside thefunction x is' , x)
#print('outside the function y is', y)