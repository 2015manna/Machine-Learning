# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:52:51 2022

@author: rakesmanna
"""

import numpy as np

a = np.arange(6)

a2 = a[np.newaxis,:]

print(a2.shape)

'''
You might occasionally hear an array referred to as a “ndarray,” which is shorthand for “N-dimensional array.”
An N-dimensional array is simply an array with any number of dimensions. You might also hear 1-D, or one-dimensional array,
2-D, or two-dimensional array, and so on. The NumPy ndarray class is used to represent both matrices and vectors.
A vector is an array with a single dimension (there’s no difference between row and column vectors), while a matrix refers
to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used.
'''
a = np.zeros(2)
print(a)

a= np.ones(2)
print(a)

a= np.empty(2)
print(a)

a= np.arange(2,9,2)
print(a)

a= np.linspace(0, 10,num=5)
print(a)

a = np.ones(2, dtype=np.int64)
print(a)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)

'''
In addition to sort, which returns a sorted copy of an array, you can use:

argsort, which is an indirect sort along a specified axis,

lexsort, which is an indirect stable sort on multiple keys,

searchsorted, which will find elements in a sorted array, and

partition, which is a partial sort.

'''

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.concatenate((a, b))

print(c)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis=0)

print(z)

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example.ndim)
print(array_example.size)
print(array_example.shape)


