# Special Pythagorean triplet (brute forced)

for a in xrange(1, 1000):
    for b in xrange(a+1, 1000):
        c = 1000 - a - b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print a, b, c, a + b + c, a * b * c

