
'''
That means the following for the expression a,b = b,a :

the right-hand side b,a is evaluated, that is to say a tuple of two elements is created in the memory. The two element are the objects designated by the identifiers b and a, that were existing before the instruction is encoutered during an execution of program
just after the creation of this tuple, no assignment of this tuple object have still been made, but it doesn't matter, Python internally knows where it is
then, the left-hand side is evaluated, that is to say the tuple is assigned to the left-hand side
as the left-hand side is composed of two identifiers, the tuple is unpacked in order that the first identifier a be assigned to the first element of the tuple (which is the object that was formely b before the swap because it had name b)
and the second identifier b is assigned to the second element of the tuple (which is the object that was formerly a before the swap because its identifiers was a)
This mechanism has effectively swapped the objects assigned to the identifiers a and b

So, to answer your question: YES, it's the standard way to swap two identifiers on two objects.
By the way, the objects are not variables, they are objects.
'''
x = 1
y = 2

print(f'{x} {y}')

x, y = y, x

print(f'{x} {y}')

a = 1
b = 2
c = 3

# not limited to a two variable swap
a, b, c = c, b, a
print(f'{a} {b} {c}')

# this is crazy
a, b, c, x, y = y, x, c, b, a



