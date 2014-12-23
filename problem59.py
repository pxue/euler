cipher = []
with open("p059_cipher.txt") as f:
    for n in f.read().strip().split(","):
        cipher.append(int(n))

# we know E is combination of three lowercase letters.
# max of a-z XOR A-Za-z is 63.
# anything else is punctuation

#punc = {}
#for c in cipher:
    #if c > 63:
        #punc.setdefault(c, 0)
        #punc[c] += 1

#from operator import itemgetter
#print sorted(punc.items(), key=itemgetter(1), reverse=True)

# highest three encoded punctuations are:
#  79, 68, 71

# let's try 71 as space
# -> first character of E is `g`

# print everything encoded with `g` that's a punctuation

#from collections import Counter
#print Counter([ch for i, ch in enumerate(cipher) if not i % 3 and ch > 63])

# the distribution makes sense:
#  71 ,73, 75 are the highest ones which are space, period and comma
# interestingly we also see 64, 78, 79: single quote and '(', ')'

# take the plain here and count all the punctuations again.
# 79 and 68 are still most frequent, maybe they are both spaces.

# d -> 68 and o -> 79
# we can see that the encryption key is "god"

pad = [ord(p) for p in "god"]
plain = []

for index, ch in enumerate(cipher):
    p = chr(pad[index % 3] ^ ch) if pad[index % 3] != 35 else ch
    plain.append(p)

print ''.join(plain), sum([ord(p) for p in plain])
