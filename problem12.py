## FACTORING Highly divisible triangular number
# find first triangular number with over 500 divisors
# triagular number = 1 + 2 + 3 .. + n

## Use Pollard's Rho Algo

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def G(x, N):
    return ((x ** 2) + 1) % N

# picks a random number pair and find one factor
def rho(N, x=2, y=2, d=1):
    while d == 1:
        x = G(x, N)
        y = G(G(y, N), N)
        d = gcd(abs(y-x), N)

    return d


from math import sqrt, ceil

def factor_c(N):
    # brute force
    f = set([1, N])
    for i in xrange(2, int(ceil(sqrt(N)))):
        d = gcd(i, N)
        if d != 1:
            f.add(d)
    return len(f) * 2

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def factor(N):
    # prime factor multiplication
    f = 1
    count = 0
    # lets try to sqrt the number
    while sqrt(N).is_integer() and N != 1:
        f = f * 3
        N = int(sqrt(N))

    for i in [2, 3, 5, 7, 11, 13, 17, 19]:
        while N % i == 0:
            N = N / i
            count+=1
        f = f * (count + 1)
        count = 0

    # if N is not 1, probably means
    # it's a prime or multiples of some prime factor
    # also check if the left over number is a perfect sqrt
    if N == 1:
        return f

    if is_prime(N):
        f = f * 2
    elif sqrt(N).is_integer():
        f = f * 3
    else:
        f = f * 4

    return f

l = 0
n = 1
t = 0
while l <= 500:
    t = n*(n+1)/2
    l = factor(t)
    n+=1

print t, l


