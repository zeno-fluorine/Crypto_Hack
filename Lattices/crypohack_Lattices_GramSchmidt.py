# Cryptohack Lattices Gram Schmidt

"""
In the last challenge we saw that there is a special kind of basis called an oorthogonal basis. Given a basis v_1, v_2, ..., v_n ∈ V for a vector space, the Gram-Schmidt algorithm calculates basis u_1, u_2, ..., u_n ∈ V

In "An introduction to Mathematical Cryptography", Jeffery Hofstein, Jill Pipher, Joseph H. Silverman, the Gram-Schmidt algorithm is given as:
    
    u_1 = v_1
    Loop i = 2,3 ..., n
        Compute μ_ij = v_i * u_j / ||u_j||^2, 1 ≤ j < i
        Set u_i = v_i - μ_ij * u_j (Sum over j for 1 ≤ j < i)
    End Loop
    
To test your code, let's grab the flag. Given the following basis vectors:

v_1 = (4,1,3,-1), v_2 = (2,1,-3,4), v_3 = (1,0,-2,7), v_4 = (6,2,9,-5)

Use the Gram-Schmidt algorithm to calculate an orthogonal basis. The flag is the float value of the second component of u_4 to 5 siginificant figures

"""

"""

Note:

Note that this algorithm doesn't create an orthonormal basis! It's a small change to implement this. Think about what you would have to change. 
If you're using someone else's algorithm and the flag is incorrect, this might be the issue. 
If everything seems good and you're still not having your answer accepted, check your rounding when you take 5.s.f. for the solution.

"""

import numpy as np

# Given basis vectors (defined as float arrays)
v_1 = np.array([4.0, 1.0, 3.0, -1.0])
v_2 = np.array([2.0, 1.0, -3.0, 4.0])
v_3 = np.array([1.0, 0.0, -2.0, 7.0])
v_4 = np.array([6.0, 2.0, 9.0, -5.0])

# List to hold the orthogonal basis vectors
u = []

# Gram-Schmidt process
def gram_schmidt(vectors):
    u = []
    for v in vectors:
        # Start with the current vector
        u_i = v.copy()
        for j in range(len(u)):
            # Compute the projection of v onto u_j
            proj = np.dot(v, u[j]) / np.dot(u[j], u[j]) * u[j]
            # Subtract the projection from u_i
            u_i -= proj
        u.append(u_i)
    return u

# List of vectors
vectors = [v_1, v_2, v_3, v_4]

# Compute the orthogonal basis
u = gram_schmidt(vectors)

# Extract the second component of u_4
second_component_u4 = u[3][1]  # u_4 is the fourth vector in the list (index 3)

# Format the output to 5 significant figures
flag = f"{second_component_u4:.5g}"

print("The flag is:", flag)
