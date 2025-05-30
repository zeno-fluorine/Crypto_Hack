# Cryptohack Lattices Size and Basis

"""

We say a set of vectors v1,v2,…,vk∈V are linearly independent if the only solution to the equation:

a1⋅v1+a2⋅v2+…+ak⋅vk=0

is for a1=a2=…=ak=0

"""

# To visualise this, think of a vector directed out of a point. Given a set of linearly independent vectors, the only way to return back to the original point is by moving along the original vector. No combination of any of the other vectors will get you there.

"""

A basis is a set of linearly independent vectors v1,v2,…,vn∈V such that any vector w∈V can be written as:

w=a1⋅v1+a2⋅v2+…+ak⋅vn​

The number of elements in the basis is also the dimension of the vector space.

We define the size of a vector, denoted ∣∣v∣∣, using the inner product of the vector with itself  ||v|| ^2 = v*v
A basis is orthogonal if for a vector basis v1,v2,…,vn∈V the inner product between any two different vectors is zero: vi⋅vj=0,i≠j

A basis is orthonormal if it is orthogonal and ∣∣v_i∣∣=1, for al  i.

"""

# That's a lot of stuff, but we'll be needing it. Time for the flag. Given the vector v = (4,6,2,5), caculate its size

import numpy as np
import math

v = np.array([4,6,2,5])
flag = np.dot(v,v)
flag = math.sqrt(flag)
print("The size of the vector is ", flag)

