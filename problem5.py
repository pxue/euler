#Smallest multiple divisible by all number between 1 to 20

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): 
    return (a * b) / gcd(a, b)

print reduce(lambda x, y: lcm(x, y), [lcm(i, i+1) for i in xrange(1, 20)])
