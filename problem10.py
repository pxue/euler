# Summation of prime smaller than 2mil

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

print reduce(lambda x, y: x + y, [p for p in xrange(2, 2000000) if is_prime(p)])
