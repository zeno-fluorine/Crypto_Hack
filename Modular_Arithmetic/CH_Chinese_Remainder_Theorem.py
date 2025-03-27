### Chinese Remainder Theorem

"""
The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers aiai, and pairwise coprime integers nini, such that the following linear congruences hold:

Note: "pairwise coprime integers" means that if we have a set of integers {n^1, n^2, ..., n^i}, all pairs of integers selected from the set are coprime: gcd(n^1, n^j) = 1

x ≡ a^1 mod n^1
x ≡ a^2 mod n^2
……
x ≡ a^n mod n^n

There is a unique solution x ≡ a mod N where N= n^1 * n^2⋅...⋅n^n

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems. """

"""

Given the following set of linear congruences:

x ≡ 2 mod 5

x ≡ 3 mod 11

x ≡ 5 mod 17

"""

# Find the integer a such that x ≡ a mod 935

"""

Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k.


x = 17j + 5, for some integer j.

Subsitute this expression for x into the congruence with the next largest modulus:

x ≡ 3 (mod 11) -> 17j + 5 ≡ 3 (mod 11)


Then solve this congruence for j:

17j + 5 ≡ 3 (mod 11)

17j ≡ -2 (mod 11)

17j ≡ 9 (mod 11)

6j ≡ 9 (mod 11)

j ≡ 18 (mod 11) (Multiply my the multiplicative inverse of 6 mod 11 (which is 2) { 6 x 2 = 12 ≡ 1 mod 11 }

j ≡ 7 (mod 11)


Rewrite this congruence as an equivalent equation:

j = 11k + 7, for some integer k


Subsitute this expression for j into the expression for x:

x = 17(11k + 9) + 5

x = 187k + 124


Now subsitute this expression for x into the final congruence, and solve the congruence for k:

187k + 124 ≡ 2 (mod 5)

187 ≡ 2 mod 5 and 124 ≡ 4 mod 5

2k + 4 ≡ 2 mod 5

2k ≡ -2 mod 5

2k ≡ 3 mod 5

k ≡ 9 mod 5

9 ≡ 4 mod 5 so

k ≡ 4 mod 5

k = 5d + 4 for some integer d

Write this congruence as an equation, and then subsitute the expression for k into the expression for x:

k = 5d + 4 for some integer d

x = 187(5d + 4) + 124 

x = 935d + 748 + 124

x = 935d + 872

This equation implies the congruence

x ≡  872 (mod 935)

This happens to be the solution to the system of congruences

"""

# Now to code this... ugh!

def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find the modular inverse of a under modulo m
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:  # No modular inverse if gcd(a, m) > 1
        return None
    if t < 0:
        t = t + m
    return t

def solve_congruences():
    # Given congruences:
    # x ≡ 2 mod 5
    # x ≡ 3 mod 11
    # x ≡ 5 mod 17

    # Step 1: Solve x ≡ 5 mod 17
    x = 17 * 0 + 5  # x = 17j + 5 for some integer j, initially j = 0

    # Step 2: Solve 17j + 5 ≡ 3 (mod 11)
    # 17j ≡ -2 (mod 11) => 17j ≡ 9 (mod 11) => 6j ≡ 9 (mod 11)
    # Find the modular inverse of 6 mod 11
    inv_6 = mod_inverse(6, 11)
    if inv_6 is None:
        return "Inverse of 6 modulo 11 does not exist!"
    j = (inv_6 * 9) % 11  # j ≡ 7 (mod 11)

    # Now substitute j = 11k + 7 into the expression for x
    x = 17 * (11 * 0 + 7) + 5  # x = 17(11k + 7) + 5 = 187k + 124

    # Step 3: Solve 187k + 124 ≡ 2 (mod 5)
    # 187k + 124 ≡ 2 (mod 5)
    # 187 ≡ 2 (mod 5), 124 ≡ 4 (mod 5)
    # 2k + 4 ≡ 2 (mod 5) => 2k ≡ 3 (mod 5)
    inv_2 = mod_inverse(2, 5)
    if inv_2 is None:
        return "Inverse of 2 modulo 5 does not exist!"
    k = (inv_2 * 3) % 5  # k ≡ 4 (mod 5)

    # Substitute k = 5d + 4 into x = 187k + 124
    x = 187 * (5 * 0 + 4) + 124  # x = 187(5d + 4) + 124 = 935d + 872

    return x % 935  # Final solution modulo 935

# Test the function
result = solve_congruences()
print(f"The solution to the system of congruences is: x ≡ {result} (mod 935)")






