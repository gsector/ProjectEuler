# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 20

# primes = [1,2,3]
# if n > 3:
#     i = 4
#     while i <= n:
#         j = 2
#         while j < i:
#             if i%j == 0:
#                 break
#             j += 1
#         if i ==j:
#             primes.append(i)
#         i+=1
# else:
#     primes = [1,2,3]

answer = 0
test = n
while answer == 0:
    j = n
    while j > 0:
        if test % j != 0:
            break
        if j == 1:
            answer = test
        j -= 1
    test += 1

print(str(answer))