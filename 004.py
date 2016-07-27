#  A palindromic number reads the same both ways.
#  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#  Find the largest palindrome made from the product of two 3-digit numbers.

import math


max_num = 999 * 999


def checkit(somenum):
    div = len(str(somenum))//2
    for i in range (0, div):
        if str(somenum)[i] != str(somenum)[len(str(somenum))-i-1]:
            return False
    return True

checknum = max_num
while checknum > 0:
    while checkit(checknum) is False:
        checknum -= 1
    num_1 = 100
    while num_1 < checknum / 100:
        num_2 = 999
        while num_2 >= num_1:
            if num_1 * num_2 == checknum:
                print(str(num_1))
                print(str(num_2))
                print(str(checknum))
                exit(0)
            num_2 += 1
        num_1 += 1
    checknum -= 1