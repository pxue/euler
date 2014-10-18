#10001st prime

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

count = 1
p = None
i = 1
while True:
    if is_prime(i):
        p = i
        if count == 10001:
            break
        count+=1

    i += 1

print p

