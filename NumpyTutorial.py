# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:30:03 2022

@author: Jose Teran
"""

# NUMPY TUTORIAL
import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Get a specific element [r,c]
b=a[0,2]

# Get a specific row
c=a[0,:]

# Get a specifig column
d=a[:,0]

# Get a specific part of the array [startindex:endindex:stepisize]
e=a[0,0:3:1]

# Modify an entire column a[:,r] or row a[r,:] with a value r

# All zeros matrix and all ones or any other number

f=np.zeros(5)
f1=np.zeros((2,5,2))

g=np.ones(10)

h=np.full(5,99)
h1=np.full_like(a,80)

# Identity matrix
I5=np.identity(5)

# Exercise
arr=np.ones((5,5))
arr[1:4,1:4]=0
arr[2,2]=9

# Operations

a=np.array([1,2,6,3])
av=np.average(a)
