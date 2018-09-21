import math
#euler 6
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumsq = sum([x*x for x in range(1,101)])
print(sumsq)
sqsum=sum(range(1,101))**2
print(sqsum)
print(sqsum-sumsq)

# 25164150
######################################################################################
#7
#8
#9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc. answer 10 18 24 = 31875000


for a in range(1,1001):
    print("a=",a)
    for b in range(a,1001):
        for c in range(b,1001):
            if (a +b +c) == 1000 and (a**2+b**2 == c**2):
                print("answer",a,b,c,"=",a*b*c)
