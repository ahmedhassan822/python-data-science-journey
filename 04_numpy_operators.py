# Arthimatics Operators
import numpy as np
arr=np.array([1.3,2.4,3.3,4.5,5.9])
print(arr)

# Adding array
print(arr+2)

# subtraction
print(arr-2)

# Multiplication
print(arr*2)

# Dividing
print(arr/2)

# Power Operation
print(arr**2)

# Matematical Operators used
print(np.sqrt(arr))

# Round off number
print(np.floor(arr))

# take the top value of fractional number
print(np.ceil(arr))

# Element wise
arr1=np.array([1,2,3,4,5,6])
arr2=np.array([11,12,13,14,15,16])

# addition
print(arr1+arr2)

# subtarction
print(arr1-arr2)

# Multiplication
print(arr1*arr2)

# Comperesion Operator
marks=np.array([45,55,34,87])
print(marks>=40 ) # answer is true or false
print(marks<40)
# setting the value
marks[3]=88
print(marks)

# setting condition
marks[marks<40]=0
print(marks)



