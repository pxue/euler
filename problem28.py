# Problem 28: number spiral diagonals
#  realize that upper right corner is odd number squared

print sum([4*(n*n) - 6*(n-1) for n in xrange(3, 1002, 2)])+1
