#  The prime factors of 13195 are 5, 7, 13 and 29.
#  What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143
primes = []
k = n


j = int(math.sqrt(n) + 1)

if n % 2 == 0:
    j = n - 1


while j > 0:
    # Keep skipping until the first factor is found that is not divisible by 2
    while n % j != 0 and j > 0:
        j -= 2

    print('Number to check: ' + str(j))

    # A factor was found - is it prime?
    k = 3
    while k < j:
        if j % k == 0 or j == k:
            print('Failed: ' + str(j) + '. Divisible by ' + str(k))
            break
        k += 2

    if j == k:
        break

    j -= 2

print('Winner is ' + str(j))