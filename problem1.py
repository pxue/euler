# Multiples of 3 and 5
print reduce(lambda x, y: x + y, [i for i in xrange(1000) if not (i % 3) or not (i % 5)])
