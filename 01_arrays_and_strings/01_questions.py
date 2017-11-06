import numpy as np

def compressString(string):
    """
    Question 1.5
    Compresses string as counts of characters.
    """
    if len(string) == 0:
        return ''
    count = 1
    compressedString = string[0]
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressedString = compressedString + str(count) + string[i]
            count = 1
    compressedString = compressedString + str(count)
    if len(string) > len(compressedString):
        return compressedString
    else:
        return string


def rotateArray(array):
    """
    Question 1.6
    Rotates an array 90 degrees counterclockwise, element-wise.
    Runtime: O(n^2), any algorithm must touch all elements
    Additional storage: O(1)
    """
    n = array.shape[0]
    for i in range(n/2):
        for j in range(i, n-i-1):
            temp = array[j,i]
            array[j,i] = array[i,n-j-1]
            array[i,n-j-1] = array[n-j-1,n-i-1]
            array[n-j-1,n-i-1] = array[n-i-1,j]
            array[n-i-1,j] = temp
    return array


def zeroRowsColumns(matrix):
    """
    Question 1.7
    Zeroes entire row and column of any zero entries in matrix.
    """
    rows = []
    columns = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 0:
                rows.append(i)
                columns.append(j)
    for row in rows:
        matrix[row,:] = 0
    for column in columns:
        matrix[:,column] = 0
    return matrix
