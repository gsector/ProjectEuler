# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

def pythtest (x, y, z, v):
    res = 'no'
    if x*x + y*y == z*z and x + y + z == v:
        res = 'pass'
    return res

def printstuff(x,y,z,v):
    print('A: ' + str(x) + ' B: ' + str(y) + ' C: ' + str(z) + ' n: ' + str(v))


n = 1000
a = 1
b = 2
c = 3

while pythtest(a,b,c,n) != 'pass':
    while c > b:
        while b > a:
            if pythtest(a,b,c,n) == 'pass':
                break
            a += 1
        if pythtest(a,b,c,n) != 'pass':
            a = 1
            b += 1
        else:
            break
    if pythtest(a,b,c,n) != 'pass':
        b = 2
        c += 1
    else:
        break

printstuff(a,b,c,n)
print(str(a*b*c))



