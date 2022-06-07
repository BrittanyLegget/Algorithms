import sys


def kth_element(Arr1, Arr2, k):
    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Decrement counter
    x = k

    # empty list to store the lower of the two values at arr[i] or arr[j]
    tempArr = []

    while x != 0:
        if i < len(Arr1) and j < len(Arr2):
            if Arr1[i] <= Arr2[j]:
                # The value from Arr1 is smaller and will added to Arr3
                tempArr.append(Arr1[i])
                # Move the iterator forward and decrement counter
                i += 1
                x -= 1
            else:
                # The value from Arr2 is smaller and will be added to Arr3
                tempArr.append(Arr2[j])
                # Move the iterator forward and decrement counter
                j += 1
                x -= 1
    # Print kth element
    return tempArr[k-1]


Arr1 = sys.argv[1].split(',')
Arr2 = sys.argv[2].split(',')
k = sys.argv[3]
print(kth_element(Arr1, Arr2, k))
