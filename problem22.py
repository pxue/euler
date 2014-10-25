# Problem22 Name scores
# Let's try no optimization
import ujson
from string import uppercase

names = []
with open("p022_names.txt", "r") as f:
    names = ujson.decode("[" + f.read() + "]")


names = sorted(names)
score = 0

for pos, name in enumerate(names, start=1):
    local_score = reduce(lambda x, y: x + y, [uppercase.index(ch)+1 for ch in name])
    score += (local_score * pos)

print score
