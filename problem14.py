# Collatz conjecture. Relevant xkcd: http://xkcd.com/710/
# Space - Time trade off

cache = {}
gmax = gkey = 0

import time
import operator

s = time.time()

for start in xrange(2, 1000000):
    if cache.get(start, None):
        continue

    n = start

    local_cache = []
    local_mod = 0
    while n != 1:
        if cache.get(n):
            local_mod = cache.get(n) - 1
            break
        else:
            local_cache.append(n)

        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1

    for i in xrange(len(local_cache)):
        f = local_cache[i]
        if not cache.get(f):
            val = len(local_cache) - i + local_mod + 1
            cache[f] = val
            if val > gmax:
                gkey = f
                gmax = val


# this is a much shorter, smarter solution
# than mine. Taken from the problem board by user lll9p
def better():
    r = {}
    r[1] = 0
    r[2] = 1
    for i in xrange(3, 1000001):
        num = i
        chain = 0
        while num not in r:
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 +1
            chain += 1
        r[i] = chain + r[num]
    print(max(r.items(), key=operator.itemgetter(1)))

## it's interesting how slow python's dictionary access in a tight for loop.


print "Completed in: %ss. Found %s to have len %s." % (time.time()-s, gkey, gmax)


