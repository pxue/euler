import time

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

l = list()

s = time.time()

end = 101
for a in xrange(2, end):
    # if number is a perfect square
    # start at upperlimit / 2
    start = 2
    if a in [4, 9, 16, 25, 36, 49, 64, 81, 100]:
        start = end/2
    elif a in [8, 27, 64]:
        start = end/3

    for b in xrange(start, end):
        l.append(a**b)

print (time.time() - s) * 10**8, len(l), len(set(l))
