'''

Iterators are objects that maintain state, use lazy evaluation, don't store sequence in memory
Iterators support a method called next()
    which yields the next value
Lists and Tuples have an iter() method which returns an iterator

Generator Function -> Returns a generator object
Generator Object -> Uses lazy evaluation to yield sequences
  A generator object is an iterator
  Not all iterators are generator objects

'''

def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# list prime numbers up to a max using yield
def list_primes(max):
    for n in range(max):
        if isPrime(n):
            yield n


for x in list_primes(20):
    print(x)

# generator objects cannot be reused
# calling next() on an exhausted generator raises an exception StopIteration
# a for loop catches this exception and terminates the loop

def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# get fibonacci sequence in a number range using yield
def fib_gen(n):
    for i in range(1, n):
        yield fib(i)


print(fib(1))
print('fib sequence')
for f in fib_gen(10):
    print(f'{f}')


# a more compact pythonic way of generating a fib sequence with yield
def fib_seq():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing+lead

print('fib sequence 2')
fib = fib_seq()
for _ in range(10):
    x = next(fib)
    print(f'{x}')
