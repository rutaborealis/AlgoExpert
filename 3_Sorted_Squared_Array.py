'''
3. Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.
'''

# 1
def sortedSquaredArray(array):
    return sorted(list(map(lambda x: x**2, array)))

#2
def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    smaller_idx = 0
    larger_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_vallue = array[smaller_idx]
        larger_value = array[larger_idx]

        if abs(smaller_vallue) > abs(larger_value):
            sorted_squares[idx] = smaller_vallue ** 2
            smaller_idx += 1
        else:
            sorted_squares[idx] = larger_value ** 2
            larger_idx -= 1

    return sorted_squares


print(sortedSquaredArray([-10, -5, 0, 5, 10]))
