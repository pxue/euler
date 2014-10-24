# Problem20: Factorial digit sum
#   find sum of factorial of 100!
# Python has builtin Math.Factorial function
#   let's see how that's implemented


# From python src code
# Divide-and-conquer factorial algorithm
#
# Based on the formula and psuedo-code provided at:
# http://www.luschny.de/math/factorial/binarysplitfact.html
#
# Faster algorithms exist, but they're more complicated and depend on
# a fast prime factorization algorithm.
#
# Notes on the algorithm
# ----------------------
#
# factorial(n) is written in the form 2**k * m, with m odd.  k and m are
# computed separately, and then combined using a left shift.
#
# The function factorial_odd_part computes the odd part m (i.e., the greatest
# odd divisor) of factorial(n), using the formula:
#
#   factorial_odd_part(n) =
#
#        product_{i >= 0} product_{0 < j <= n / 2**i, j odd} j
#
# Example: factorial_odd_part(20) =
#
#        (1) *
#        (1) *
#        (1 * 3 * 5) *
#        (1 * 3 * 5 * 7 * 9)
#        (1 * 3 * 5 * 7 * 9 * 11 * 13 * 15 * 17 * 19)
#
# Here i goes from large to small: the first term corresponds to i=4 (any
# larger i gives an empty product), and the last term corresponds to i=0.
# Each term can be computed from the last by multiplying by the extra odd
# numbers required: e.g., to get from the penultimate term to the last one,
# we multiply by (11 * 13 * 15 * 17 * 19).
#
# To see a hint of why this formula works, here are the same numbers as above
# but with the even parts (i.e., the appropriate powers of 2) included.  For
# each subterm in the product for i, we multiply that subterm by 2**i:
#
#   factorial(20) =
#
#        (16) *
#        (8) *
#        (4 * 12 * 20) *
#        (2 * 6 * 10 * 14 * 18) *
#        (1 * 3 * 5 * 7 * 9 * 11 * 13 * 15 * 17 * 19)
#
# The factorial_partial_product function computes the product of all odd j in
# range(start, stop) for given start and stop.  It's used to compute the
# partial products like (11 * 13 * 15 * 17 * 19) in the example above.  It
# operates recursively, repeatedly splitting the range into two roughly equal
# pieces until the subranges are small enough to be computed using only C
# integer arithmetic.
#
# The two-valuation k (i.e., the exponent of the largest power of 2 dividing
# the factorial) is computed independently in the main math_factorial
# function.  By standard results, its value is:
#
#    two_valuation = n//2 + n//4 + n//8 + ....
#
# It can be shown (e.g., by complete induction on n) that two_valuation is
# equal to n - count_set_bits(n), where count_set_bits(n) gives the number of
# '1'-bits in the binary expansion of n.
#/

# factorial_partial_product: Compute product(range(start, stop, 2)) using
# divide and conquer.  Assumes start and stop are odd and stop > start.
# max_bits must be >= bit_length(stop - 2).

from math import factorial

print reduce(lambda x, y: x + y, [int(i) for i in str(factorial(100))])

