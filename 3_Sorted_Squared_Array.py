'''
3. Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.
'''

# 1
def sortedSquaredArray(array):
    return sorted(list(map(lambda x: x**2, array)))
