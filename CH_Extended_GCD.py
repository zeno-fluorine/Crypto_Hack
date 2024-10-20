### Extended GCD

""" Let aa and bb be positive integers.

The extended Euclidean algorithm is an efficient way to find integers u,v such that

a⋅u+b⋅v=gcd⁡(a,b)a⋅u+b⋅v=gcd(a,b)

Using the two primes p=26513,q=32321p=26513,q=32321, find the integers u,vu,v such that

p⋅u+q⋅v=gcd⁡(p,q)p⋅u+q⋅v=gcd(p,q)

Enter whichever of u and v is the lower number as the flag.

HINT: Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.
HINT: Knowing that p,qp,q are prime, what would you expect gcd⁡(p,q)gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.

"""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Given primes
p = 26513
q = 32321

# Calculate the Extended GCD
gcd, u, v = extended_gcd(p, q)

# Output the results
print(f"GCD: {gcd}, u: {u}, v: {v}")

# Find the lower value
flag = min(u, v)
print(f"Flag: {flag}")
