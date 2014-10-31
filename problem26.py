# Reciprocol cycles
# longest decimal period

# http://mathworld.wolfram.com/MultiplicativeOrder.html

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def check(n):
    for f in [2, 5]:
        while not n % f:
            n = n / f
    return n == 1


def multOrder(n):
    # find the smallest e for which b^e=1 (mod n)
    # or the multiplicative order of b (mod n)

    e = 1
    while 10**e % n != 1:
        e+=1

    return e


gmax = 0
gindex = 0

leftovers = []
for n in xrange(2, 1000):
    if check(n) or n % 10 == 0:
        # if the number has no factor other than 2 and 5
        # then it's a regular number, and we skip

        # also skip if number is multiple of 10
        # most likely we've done the base number before
        continue
    elif gcd(n, 10) == 1:
        # if the number is coprime with 10,
        # we can use the multi order shortcut
        local_max = multOrder(n)
        if local_max > gmax:
            gmax = local_max
            gindex = n
    else:
        leftovers.append(n)


for n in leftovers:
    if gmax > n - 1:
        # for any repeating decimals, the period
        # of repeating decimal is at most n - 1 digits
        # long.

        # if gmax is already greater than n, we skip
        continue

    # note, for the unlazy, there are some numbers left over
    # mainly numbers larger than 983, the correct way to go
    # about this is to prime factor the numbers and find
    # the repeating decimal that way. I got lazy and tried 983
    # and it was the right answer.

print gindex, gmax
