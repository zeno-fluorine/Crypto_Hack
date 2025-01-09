### Quadratic Residues

"""
We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p=29p=29. We can take the integer a=11a=11 and calculate a2=5mod  29a2=5mod29.

As a=11,a2=5a=11,a2=5, we say the square root of 55 is 1111.

This feels good, but now let's think about the square root of 1818. From the above, we know we need to find some integer aa such that a2=18a2=18

Your first idea might be to start with a=1a=1 and loop to a=p−1a=p−1. In this discussion pp isn't too large and we can quickly check all options.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a∈Fp∗a∈Fp∗​ you never find an aa such that a2=18a2=18.

What we are seeing, is that for the elements of Fp∗Fp∗​, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp∗Fp∗​, there is no square root.

In other words, xx is a quadratic residue when it is possible to take the square root of xx modulo an integer pp.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

"""

"""
HINT: We say that an integer xx is a Quadratic Residue if there exists an aa such that a2≡xmod  pa2≡xmodp. If there is no such solution, then the integer is a Quadratic Non-Residue.

HINT: If a2=xa2=x then (−a)2=x(−a)2=x. So if xx is a quadratic residue in some finite field, then there are always two solutions for a.

"""

def find_quadratic_residues(p):
    residues = {}
    for a in range(p):
        square = (a * a) % p
        if square not in residues:
            residues[square] = []
        residues[square].append(a)
    return residues

def main():
    p = 29
    ints = [14, 6, 11]
    
    residues = find_quadratic_residues(p)
    
    for x in ints:
        if x in residues:
            roots = residues[x]
            print(f"{x} is a quadratic residue of {p}. Square roots are: {roots}.")
        else:
            print(f"{x} is a quadratic non-residue of {p}.")

if __name__ == "__main__":
    main()
