# power digit sum

print reduce(lambda x, y: x+y, [int(d) for d in str(2 << 999)])


