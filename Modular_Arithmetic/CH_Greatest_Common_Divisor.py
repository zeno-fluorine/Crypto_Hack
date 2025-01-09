### Modular Arithmetic Greatest Common Divisor

""" The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b)(a,b).

For a=12,b=8a=12,b=8 we can calculate the divisors of aa: {1,2,3,4,6,12}{1,2,3,4,6,12} and the divisors of bb: {1,2,4,8}{1,2,4,8}. Comparing these two, we see that gcd⁡(a,b)=4gcd(a,b)=4.

Now imagine we take a=11,b=17a=11,b=17. Both aa and bb are prime numbers. As a prime number has only itself and 11 as divisors, gcd⁡(a,b)=1gcd(a,b)=1.

We say that for any two integers a,ba,b, if gcd⁡(a,b)=1gcd(a,b)=1 then aa and bb are coprime integers.

If a and b are prime, they are also coprime. If aa is prime and b<ab<a then aa and bb are coprime.

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.

Try coding it up; it's only a couple of lines. Use a=12,b=8a=12,b=8 to test it.

Now calculate gcd⁡(a,b)gcd(a,b) for a=66528,b=52920a=66528,b=52920 and enter it below. """


""" HINT: Think about the case for a prime and b>a, why are these not necessarily coprime? """


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 66528
num2 = 52920
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")
