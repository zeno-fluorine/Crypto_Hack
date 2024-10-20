### Modular Arithmetic 2

"""
We'll pick up from the last challenge and imagine we've picked a modulus pp, and we will restrict ourselves to the case when pp is prime.

The integers modulo pp define a field, denoted Fp.

A finite field FpFp​ is the set of integers 0,1,...,p−10,1,...,p−1, and under both addition and multiplication there are inverse elements b+b+​ and b∗b∗​ for every element aa in the set, such that a+b+=0a+b+​=0 and a⋅b∗=1a⋅b∗​=1.

Lets say we pick p=17p=17. Calculate 317mod  17317mod17. Now do the same but with 517mod  17517mod17.

What would you expect to get for 716mod  17716mod17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

Now take the prime p=65537p=65537. Calculate 27324678765465536mod  6553727324678765465536mod65537.

Did you need a calculator?

"""

"""
HINT: If the modulus is not prime, the set of integers modulo n define a ring.
HINT: Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: a+0=a and a⋅1=a.

"""

# Define the values
base = 273246787654
exponent = 65536
modulus = 65537

# Calculate the result using modular exponentiation
result = pow(base, exponent, modulus)

# Print the result
print(result)

