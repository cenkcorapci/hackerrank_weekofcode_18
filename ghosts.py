#!/bin/python

import sys


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


towns, streets, houses, apartments = [int(x) for x in raw_input().strip().split(' ')]

ghosts = 0
for town in xrange(1, towns + 1):
    for street in xrange(1, streets + 1):
        for house in xrange(1, houses + 1):
            for apartment in xrange(1, apartments + 1):
                if (town - street) % 3 != 0:
                    continue
                if (street + house) % 5 != 0:
                    continue
                if (town * house) % 4 != 0:
                    continue
                if gcd(town, apartment) != 1:
                    continue
                #print "ok: ", town, " ", street, " ", house, " ", apartment
                ghosts += 1

print ghosts
