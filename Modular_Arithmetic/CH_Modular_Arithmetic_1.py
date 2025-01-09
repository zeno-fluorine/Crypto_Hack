### Modular Arithmetic: Modular Arithmetic 1

"""
Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:

4 + 9 = 1
5 - 7 = 10
2 + 3 = 5

At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).

Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a≡bmod  ma≡bmodm.

Another way of saying this, is that when we divide the integer a by m, the remainder is bb. This tells you that if mm divides aa (this can be written as m∣am∣a) then a≡0mod  ma≡0modm.

Calculate the following integers:

11≡xmod  611≡xmod6
8146798528947≡ymod  178146798528947≡ymod17

The solution is the smaller of the two integers, (x,y)(x,y), you obtained after reducing by the modulus.
"""

# Define the numbers and moduli
num1 = 11
mod1 = 6

num2 = 8146798528947
mod2 = 17

# Calculate x = num1 mod mod1
x = num1 % mod1

# Calculate y = num2 mod mod2
y = num2 % mod2

# Find the smaller of the two values
result = min(x, y)

# Print the results
print("x (11 mod 6):", x)
print("y (8146798528947 mod 17):", y)
print("Smaller value:", result)
