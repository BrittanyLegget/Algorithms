import argparse

CLI = argparse.ArgumentParser()
CLI.add_argument(
    "--list1",
    nargs="*",
    type=int,
    default=[4, 6, 9, 11, 16, 17, 23],  # default if nothing is provided
)
CLI.add_argument(
    "--list2",
    nargs="*",
    type=int,
    default=[1, 1, 1, 3, 7, 9, 11, 18, 20],
)
CLI.add_argument(
    "--k",
    nargs="*",
    type=int,
    default=[12],
)


def kth_element(Arr1, Arr2, k):
    if len(Arr1) + len(Arr2) < k:
        return "Error: the value of k cannot be greater than the number if items in the lists combined."

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
    return tempArr[k - 1]


args = CLI.parse_args()
Arr1 = args.list1
Arr2 = args.list2
k = args.k[0]
print(kth_element(Arr1, Arr2, k))
