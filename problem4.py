#Largest palindrome product
def palindrome(p):
    return str(p) == str(p)[::-1]

P = set()
for x in xrange(100, 999):
    for y in xrange(x+1, 999):
        p = x * y
        if palindrome(p):
            P.add(p)

print max(P)
