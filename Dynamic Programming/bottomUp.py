# Dynamic Programming Bottom-up approach to determine the longest continuous substring.


def lcs_bottomup(charList1, charList2):
    m = len(charList1)
    n = len(charList2)

    # Initialize 2D array with 0's
    LCS = [[0 for i in range(m+1)] for j in range(n+1)]

    # Iterate through the strings
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif charList1[i-1] == charList2[j-1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    return LCS[i][j]
