### Modular Inverting

"""
As we've seen, we can work within a finite field Fp​, adding and multiplying elements, and always obtain another element of the field.

For all elements gg in the field, there exists a unique integer dd such that g⋅d≡1mod  pg⋅d≡1modp.

This is the multiplicative inverse of g.

Example: 7⋅8=56≡1mod  117⋅8=56≡1mod11

What is the inverse element: d=3^−1 such that 3⋅d≡1mod  13?
"""

"""
HINT: Think about the little theorem we just worked with. How does this help you find the inverse of an element?
""" 


def modular_inverse(g, p):
    # Using Fermat's Little Theorem
    return pow(g, p - 2, p)

# Given values
g = 3
p = 13

# Calculate the inverse
d = modular_inverse(g, p)
print(f"The multiplicative inverse of {g} mod {p} is: {d}")
