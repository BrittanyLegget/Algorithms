# Dynamic Programming top-down approach to determine the longest continuous substring.


def lcs_topdown(charList1, charList2, i, j, topdown):
    m = len(charList1)
    n = len(charList2)

    if i == n or j == m:
        return 0
    # If we have already calculated this position, return value already computed
    if topdown[i][j] != -1:
        return topdown[i][j]
    # If equal, store the value in topdown
    if charList1[i] == charList2[j]:
        topdown[i][j] = lcs_topdown(
            charList1, charList2, i + 1, j + 1, topdown) + 1
    else:
        # Store the one with the largest value in topdown
        topdown[i][j] = max(lcs_topdown(charList1, charList2, i, j + 1,
                            topdown), lcs_topdown(charList1, charList2, i + 1, j, topdown))
    return topdown[i][j]


# Helper function to initialize array and pass to lcs_topdown procedure
def lcs_topdown_helper(charList1, charList2):
    m = len(charList1)
    n = len(charList2)

    # Initialize 2D array with -1's
    topdown = [[-1 for i in range(m+1)] for j in range(n+1)]
    return lcs_topdown(charList1, charList2, 0, 0, topdown)
