#!/usr/local/bin/python3






def array_left_rotation(a, n, k):
    if n == 0 or k == 0:
        return a
    def gcd(a,b):
        while( a != 0 ):
            c = a
            a = b % a
            b = c
        return b
    k = n % k
