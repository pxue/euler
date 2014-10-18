# Sum square difference
x = reduce(lambda x, y: x + y, [i for i in xrange(1,101)]) ** 2
y = reduce(lambda x, y: x + y, map(lambda x: x**2, [i for i in xrange(1,101)]))

print x - y
