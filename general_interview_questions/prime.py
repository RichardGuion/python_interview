
# determine if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 5
if isPrime(n):
    print(f'{n} is prime number')
else:
    print(f'{n} is not prime number')


# find prime numbers from o to 99
def list_primes():
    for n in range(100):
        if isPrime(n):
            print(n, end=' ', flush=True)

list_primes()

