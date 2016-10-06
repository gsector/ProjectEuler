# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

n = 10001

primeCount = 3
nprime = 0
i = 6

while primeCount < n:
    j = 2
    while j < i:
        if i % j == 0:
            break
        if j == i-1:
            primeCount += 1
        if primeCount == n:
            nprime = i
        j += 1
    i += 1

print(str(nprime))