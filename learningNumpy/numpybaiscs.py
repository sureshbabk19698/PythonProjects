import numpy as np
import numpy.random as rd

print("Array initialization in array vs numpy array")
array = [10, 11, 12, 13]
print(array)
npArray = np.array(array)
print(npArray)

# key differences
print("Logical Operations in entire array without looping")
print(npArray > 5)  # [ True  True  True  True]
# print(array > 5) # TypeError: '>' not supported between instances of 'list' and 'int'
print("Mathematical Operations in np array")
print("Sum", npArray.sum())
twoDnpArray = np.arange(25, 50).reshape(5, 5)
print("Sum of 2D array columns: ", twoDnpArray.sum(axis=1))
print("Slicing from 2D array columns: ", twoDnpArray[3:, 3:])
print("Sqrt of array values [10, 11, 12, 13]: ", npArray ** 3)

print("Slicing in normal array vs npArray ")
a, b = array[0:2]
print(a, b)
print(array)

a, b = npArray[0:2]
print(a, b)
print(npArray)

twoDlist = [[1, 2, 3], [1, 2, 3]]
print(twoDlist)
npArray = np.array(twoDlist)
print(npArray)

print("Features in numpy array ")
print("Create  array with start and stop values and with step size: ", np.arange(0, 10, step=1))  # 0, 1, 2...9
print("generate 4 * 5 matrix with all values as 0", np.zeros((4, 5)))
print("generate 4 * 5 matrix with all values as 1", np.ones((4, 5)))

print("5, 10 , 15 - Evenly distribute betweens start and stop", np.linspace(5, 15, 3))

print("generate identical matrix", np.eye(4))
# [1, 0 , 0, 0
#  0, 1, 0, 0 ]...

print("Generate two random numbers in array ", rd.rand(2))  # [0.161919  0.1551505]
print("Generate two random numbers in 2D array ", rd.rand(2, 2))
# [[0.58857366 0.10891324]
# [0.23165265 0.61074678]]

print("Generate 5 random numbers between low and high values: ", rd.randint(1, 10, 5))

arr = np.arange(25, 50)
print("Reshape array m * n matrix", arr.reshape(5, 5))
print("Shape of the matrix", arr.reshape(5, 5).shape)

print("Index of maximum number", arr.argmax())  #
print("Maximum number", arr.max())  # max number
