numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 0
primes = []
not_primes =[]
for i in numbers:
    is_prime = True
    if i < 2:
        continue
    for x in range(2, (i // 2) + 1):
        if i % x == 0:
            is_prime = False

    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(not_primes)
print (primes)