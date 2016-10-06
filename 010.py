# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from datetime import datetime
import sympy

start_time = datetime.now()
n = 2000000
step = 0.10


sumnum = 0
step_orig = step

for j in range(1,n):
    if j == int(n*step):
        print('Percent Complete: ' + str(1.0*j/n))
        print('Running for: ' + str(datetime.now()-start_time))
        print('-')
        step += step_orig

    if sympy.isprime(j) == True:
        sumnum += j
print('----------------' + '\n')
print('Sum of Primes: ' + str(sumnum))
print('It took ' + str(datetime.now()-start_time))
