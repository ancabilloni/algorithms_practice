"""
Fast multiplication. Run time O(n^log_2(3)), better improvement from Brute force O(n^2)
Applying Divide & Conquer

"""

from math import floor, ceil

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x*y
    
    n_size = max(len(str(x)), len(str(y)))
    m_size = ceil(float(n_size/2))
    
    a = int(floor(x/10**m_size))
    b = int(floor(x%10**m_size))
    
    c = int(floor(y/10**m_size))
    d = int(floor(y%10**m_size))
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    
    ad_bc = karatsuba(a+b, c+d) - ac - bd
    
    return int(ac*10**(m_size*2) + ad_bc*10**m_size + bd)

print (karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                 2718281828459045235360287471352662497757247093699959574966967627))
