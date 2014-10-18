#Largest prime factor
from math import sqrt, ceil, pow

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

C = 600851475143

def G(n):
    return ((n ** 2) + 1) % C

def factor(n, x=2, y=2, d=1):
    f = []
    while d < n:
        x = G(x)
        y = G(G(y))

        d = gcd(abs(x - y), n)
        if d != 1 and d not in f:
            print d
            f.append(d)

    return f

f = factor(C)
print sorted([p for p in f if is_prime(p)])
