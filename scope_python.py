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


print('==============================================================')

x = 1
y = 1

def foo1(x):
    print(f'x inside the function foo us {x}, thisis local x')
    x = 5
    print(f'x inside function foo is {x}, this is a local x')

def foo_adv():
    # 1. access field value before putting new value
    #    field is read - only! be carefull!
    print(f'x inside foo_avd {x}')  # local x not found, global x will be used
    x = 10  # craash!!v
    print(f'x inside foo_avd {x}')


def foo_adv_new_x():
    # 2. access field first time with new value
    #    field is local!!!
    x = 10  # this will make a local x
    print(f'x inside foo_avd {x}')


def foo_global_x():
    # 3. the function x will be same as global
    global x
    x = 77

    # foo(3)
    # foo(x)
    # foo_adv_read_only()


foo_adv_new_x()
foo_global_x()
print('outside the function - global scope, the x is', x)
print('outside the function - global scope, the y is', y)

print('outside the function = global scope, the x is', x)
print('outside the function = global scope the y is', y)

