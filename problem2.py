# Even Fibonacci numbers
f = [0, 1]

for i in xrange(1, 100):
    n = f[i-1] + f[i]
    if n > 4000000:
        break
    f.append(n)

print reduce(lambda x, y: x + y, [i for i in f[2:] if not i % 2])


