import numpy as np

# initializing one dimentional array 
n1 = np.array([1,2,3,4,5])
print(n1)

# Output
# array([1,2,3,4,5])

# initializing two dimentional array 
n1 = np.array([[12,43,54],[4,3,2]])
print(n1)

# Output
# array([[12,43,54],
#        [41,36,27]])

# initializing multi dimentional array 
n1 = np.array([[[2,3,4],[4,3,2]],[[4,3,2],[2,45,6]]])
print(n1)

# Output
# array([[[2,3,4],[4,3,2]],
#       [[4,3,2],[2,45,6]]])

# initializing array with zeros 
n1 = np.zeros((2,2))
print(n1)


# Output
# array([[0., 0.],
#        [0., 0.]])

# initializing array with different values
n1 = np.full((2,4),34)
print(n1) 

# Output
#array([[34, 34, 34, 34],
#       [34, 34, 34, 34]])

# initializing array within range
n1=np.arange(12,23)
print(n1) 

# Output
# array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

# initializing array with random values

n1=np.random.randint(2,6,100)
print(n1) 

# Output
# array([4, 5, 3, 5, 4, 4, 4, 4, 5, 3, 5, 5, 5, 2, 3, 2, 4, 5, 4, 4, 2, 2,
#        5, 3, 3, 5, 4, 2, 2, 3, 3, 4, 3, 5, 4, 3, 5, 5, 4, 4, 2, 5, 5, 4,
#        2, 4, 2, 4, 5, 5, 3, 2, 4, 5, 5, 4, 4, 2, 5, 3, 5, 4, 4, 5, 3, 4,
#        2, 4, 2, 3, 3, 2, 3, 4, 4, 5, 4, 4, 5, 3, 3, 2, 4, 3, 3, 2, 5, 4,
#        3, 3, 4, 4, 2, 5, 3, 2, 3, 2, 3, 4])


#Operations on Numpy

n1=np.array([[12,23,45],[0,4,2,],[5,13,56]])
print(n1.shape)

#(3, 3)

n1=np.array([[12,34,56],[145,7,8]])
n2=np.array([[11,35,6],[45,67,89]])
np.vstack((n1,n2))


# array([[ 12,  34,  56],
#        [145,   7,   8],
#        [ 11,  35,   6],
#        [ 45,  67,  89]])


n1=np.array([[12,34,56],[145,7,8]])
n2=np.array([[11,35,6],[45,67,89]])
np.hstack((n1,n2))

# array([[ 12,  34,  56,  11,  35,   6],
#        [145,   7,   8,  45,  67,  89]])

n1=np.array([[12,34,56],[145,7,8]])
n2=np.array([[11,35,6],[45,67,89]])
np.column_stack((n1,n2))

# array([[ 12,  34,  56,  11,  35,   6],
#        [145,   7,   8,  45,  67,  89]])

n1=np.array([12,34,56])
n2=np.array([11,34,6])
np.intersect1d(n1,n2)

# array([34])

n1=np.array([12,34,56])
n2=np.array([11,34,6])
np.setdiff1d(n1,n2)

# array([12, 56])

print(n1)

# Numpy Mathematics

n1=np.array([12,34,56])
n2=np.array([11,34,6])
np.sum([n1,n2])
print(n1)

# output
# 153

n1=np.array([12,34,56])
n2=np.array([11,34,6])
np.sum([n1,n2],axis=0)
print(n1)

# output
# array([23, 68, 62])

n1=np.array([12,34,56])
n2=np.array([11,34,6])
np.sum([n1,n2],axis=1)
print(n1)

# output
# array([102,  51])

n1=np.array([12,34,56])
n1=n1+100
print(n1)

# output
# array([112, 134, 156])

n1=np.array([12,34,56])
n1=n1-100
print(n1)

# output
# array([-88, -66, -44])

n1=np.array([12,34,56])
n1=n1*100
print(n1)

# output
# array([1200, 3400, 5600])

n1=np.array([12,34,56])
n1=n1/100
print(n1)

# output
# array([0.12, 0.34, 0.56])

n1=np.array([12,34,56])
np.mean(n1)
print(n1)

# output
# 34.0

n1=np.array([12,34,56])
np.std(n1)
print(n1)

# output
# 17.962924780409974

# Numpy Matrix

n1=np.array([[12,34,56],[1,4,6],[3,8,0]])
print(n1[0])

# output
# array([12, 34, 56])

print(n1[:])

# output
# array([[12, 34, 56],
    #    [ 1,  4,  6],
    #    [ 3,  8,  0]])

print(n1[0:1])

# output
# array([[12, 34, 56]])

print(n1[0:,2])

# output
# array([56,  6,  0])

print(np.transpose(n1))

# output
# array([[12,  1,  3],
    #    [34,  4,  8],
    #    [56,  6,  0]])

n1=np.array([[12,34,56],[1,4,6],[3,8,0]])
n2=np.array([[12,34,56],[1,4,6],[3,8,0]])
print(n1.dot(n2))

# output
# array([[346, 992, 876],
    #    [ 34,  98,  80],
    #    [ 44, 134, 216]])

n1=np.array([[12,34,56],[1,4,6],[3,8,0]])
n2=np.array([[12,34,56],[1,4,6],[3,8,0]])
print(n2.dot(n1))

# output
# array([[346, 992, 876],
    #    [ 34,  98,  80],
    #    [ 44, 134, 216]])